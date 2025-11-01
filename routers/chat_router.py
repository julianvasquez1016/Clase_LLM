from fastapi import APIRouter
from schemas.chat_schemas import InputMessage
from services import chat_service

router = APIRouter()

@router.post("/ai-chat")
def ai_chat(data_in:InputMessage):
    

    response = chat_service.get_chat_response(data_in)
    return{"responde": response}