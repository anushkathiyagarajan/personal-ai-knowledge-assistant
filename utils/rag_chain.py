import os
from dotenv import load_dotenv
from google import genai
from utils.prompts import RAG_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(context, question):
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text