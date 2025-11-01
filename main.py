from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import chat_router, rag_router
from fastapi.responses import FileResponse
import os

app = FastAPI()

app.include_router(chat_router.router)
app.include_router(rag_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta la carpeta 'static' (donde está tu index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Sirve el index.html directamente al entrar a la raíz del sitio
@app.get("/")
async def root():
    return FileResponse("static/index.html")
