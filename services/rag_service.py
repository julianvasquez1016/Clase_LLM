from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

def get_rag_response(message: str, file_content: str):
    """
    Usa el contenido del archivo como información base (contexto)
    para responder la pregunta del usuario con el modelo de OpenAI.
    """

    try:
        # Construimos el prompt con contexto
        system_prompt = (
            "Eres un asistente experto que usa el contenido proporcionado "
            "como fuente de información para responder preguntas de forma "
            "clara, breve y en español. Si el contexto no contiene la respuesta, "
            "indica que no tienes suficiente información."
        )

        context = (
            f"Contexto (archivo de texto):\n{file_content[:6000]}"  # límite por seguridad
            if file_content else "No se proporcionó archivo de contexto."
        )

        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "assistant", "content": context},
                {"role": "user", "content": message},
            ],
        )

        response = completion.choices[0].message.content
        return response

    except Exception as e:
        print(f"Error comunicándose con OpenAI: {e}")
        return "Hubo un error al comunicarse con el modelo."
