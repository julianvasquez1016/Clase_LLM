from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import chat_router, rag_router
import os

app = FastAPI()

# Routers
app.include_router(chat_router.router)
app.include_router(rag_router.router)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia a ["http://127.0.0.1:5500"] si tienes frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carpeta static para servir archivos HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint principal que devuelve el HTML
@app.get("/")
async def root():
    return FileResponse(os.path.join("static", "rag_chat.html"))

# Endpoint de prueba
@app.get("/hello")
async def index():
    return {"message": "Hello, World!"}
