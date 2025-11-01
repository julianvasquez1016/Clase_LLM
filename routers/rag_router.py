from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from services import rag_service

router = APIRouter()

@router.post("/rag-chat")
async def rag_chat(message: str = Form(...), file: UploadFile = None):
    """
    Endpoint que recibe un mensaje y un archivo .txt (opcional).
    Usa el contenido del archivo como base de conocimiento
    para responder usando OpenAI vía OpenRouter.
    """
    if file and not file.filename.endswith(".txt"):
        return JSONResponse(
            status_code=400,
            content={"error": "Solo se permiten archivos .txt"}
        )

    file_content = ""
    if file:
        file_content = (await file.read()).decode("utf-8")

    # Llamamos al servicio que usa OpenAI
    response = rag_service.get_rag_response(message, file_content)

    return {
        "message_in": message,
        "file_name": file.filename if file else None,
        "response": response
    }
