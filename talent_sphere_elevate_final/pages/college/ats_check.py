import streamlit as st
import json
import re

from pypdf import PdfReader
from docx import Document

from AI.ai_helper import ask_gemini


def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(uploaded_file):

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text


def extract_resume_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    else:
        return ""


def analyze_resume(resume_text, job_description=""):

    prompt = f"""
You are an expert ATS resume evaluator and college placement recruiter.

Analyze the ACTUAL CONTENT of the resume below.

Do NOT give points simply because a section heading exists.

Evaluate:
1. Resume quality
2. Skills
3. Projects
4. Education
5. Experience/internships
6. Achievements
7. Technical relevance
8. Quantifiable impact
9. ATS keyword relevance
10. Formatting/readability based on the extracted text
11. Overall placement readiness

Give an ATS score from 0 to 100 based on the QUALITY and RELEVANCE
of the actual content.

A resume with headings but weak or empty content must receive a low score.

A strong resume with meaningful projects, relevant skills,
achievements, internships and measurable results should receive
a higher score.

Return ONLY valid JSON in this format:

{{
    "ats_score": 0,
    "summary": "short overall evaluation",
    "strengths": [
        "strength 1",
        "strength 2",
        "strength 3"
    ],
    "weaknesses": [
        "weakness 1",
        "weakness 2",
        "weakness 3"
    ],
    "missing_skills": [
        "skill 1",
        "skill 2"
    ],
    "improvements": [
        "improvement 1",
        "improvement 2",
        "improvement 3"
    ],
    "placement_readiness": "Low / Moderate / Good / Excellent"
}}

Job Description:
{job_description}

Resume:
{resume_text}
"""

    response = ask_gemini(prompt)

    return response


def clean_json_response(response):

    response = response.strip()

    response = re.sub(r"```json", "", response)
    response = re.sub(r"```", "", response)

    return response.strip()


def show_ats_check():

    st.title(" AI Resume Analyzer")

    st.write(
        "Upload your resume and let AI evaluate the actual content "
        "for ATS and placement readiness."
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        help="Upload your resume in PDF or DOCX format."
    )

    job_description = st.text_area(
        "Target Job Description (Optional)",
        placeholder="Paste the job description here for more relevant ATS analysis..."
    )

    if uploaded_file:

        st.success(f"Uploaded: {uploaded_file.name}")

        if st.button(
            " Analyze Resume with AI",
            use_container_width=True
        ):

            with st.spinner(
                "AI is reading and analyzing your resume..."
            ):

                try:

                    resume_text = extract_resume_text(uploaded_file)

                    if not resume_text.strip():

                        st.error(
                            "❌ Could not extract text from this resume."
                        )
                        st.info(
                            "If this is a scanned/image-only PDF, "
                            "please upload a text-based PDF or DOCX."
                        )
                        return

                    if len(resume_text.strip()) < 100:

                        st.warning(
                            "⚠️ Very little text was found in the resume. "
                            "The ATS analysis may not be reliable."
                        )

                    result = analyze_resume(
                        resume_text,
                        job_description
                    )

                    result = clean_json_response(result)

                    data = json.loads(result)

                    st.session_state.resume_analysis = data

                except json.JSONDecodeError:

                    st.error(
                        "❌ AI returned an unexpected format. "
                        "Please try analyzing the resume again."
                    )

                except Exception as e:

                    st.error(
                        f"❌ Resume analysis failed: {str(e)}"
                    )

    if "resume_analysis" in st.session_state:

        data = st.session_state.resume_analysis

        st.divider()

        st.subheader(" ATS Score")

        score = data.get("ats_score", 0)

        st.metric(
            "AI ATS Score",
            f"{score}/100"
        )

        st.progress(
            min(max(score, 0), 100) / 100
        )

        st.subheader(" Overall Evaluation")

        st.write(
            data.get(
                "summary",
                "No summary available."
            )
        )

        st.subheader("Strengths")

        strengths = data.get("strengths", [])

        for item in strengths:
            st.write(f"• {item}")

        st.subheader(" Weaknesses")

        weaknesses = data.get("weaknesses", [])

        for item in weaknesses:
            st.write(f"• {item}")

        st.subheader(" Missing Skills")

        missing_skills = data.get("missing_skills", [])

        if missing_skills:

            for item in missing_skills:
                st.write(f"• {item}")

        else:

            st.write("No major missing skills identified.")

        st.subheader(" Recommended Improvements")

        improvements = data.get("improvements", [])

        for item in improvements:
            st.write(f"• {item}")

        st.subheader(" Placement Readiness")

        st.info(
            data.get(
                "placement_readiness",
                "Not available"
            )
        )
    st.divider()

    if st.button("⬅ Back to Student Features", use_container_width=True):
        st.session_state.page = "student_features"
        st.rerun()