from schemas.chat_schemas import InputMessage
from openai import OpenAI
from dotenv import load_dotenv
import os

#pip omstaññ python-detenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)
def get_chat_response(data_in: InputMessage):
    data = data_in.model_dump()
    message = data["message"]

    try:
        #Aqui llamamos al modelo y obtenemos response
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {"role": "system",
                "content": "Eres un asistente que siempre responde en español de forma clara y breve"
                },
                {
                    "role":"user",
                    "content":message
                }
            ])
        print(completion.choices[0].message.content)
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        print (f"Error communitacting with OpenAI: {e}")
        return "Error communitacting with OpenAI"
    