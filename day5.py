import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Add GEMINI_API_KEY to the .env file before running this program.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.6-flash"
TRIAGE_PROMPT = """You are a symptom triage assistant, not a doctor.
Classify urgency as LOW, MEDIUM, HIGH, or EMERGENCY, and always include a
disclaimer that this is not a diagnosis. For emergency symptoms, tell the user
to seek emergency care immediately."""


def triage(symptom_description: str) -> str:
    """Return non-diagnostic urgency guidance for a symptom description."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=symptom_description,
            config=types.GenerateContentConfig(
                system_instruction=TRIAGE_PROMPT,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                ),
            ),
        )
    except httpx.HTTPError as error:
        raise RuntimeError(
            "Could not reach the Gemini API. Check your internet connection or proxy."
        ) from error

    return response.text or "The model returned no text. Please try again."


if __name__ == "__main__":
    try:
        print(triage("I've been feeling dizzy since yesterday."))
    except RuntimeError as error:
        print(f"Error: {error}")
