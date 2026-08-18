import os

from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()


# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")


# Check API key
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to the .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text