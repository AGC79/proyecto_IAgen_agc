import os
from groq import Groq
from config_env import Config

client = Groq(api_key=Config.GROQ_API_KEY)

def get_answer(question: str) -> str:
    """
    Envía la pregunta al modelo Groq y devuelve la respuesta.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": question}
        ],
        model="llama-3.3-70b-versatile",  # puedes cambiar a otro modelo Groq
    )
    return chat_completion.choices[0].message.content