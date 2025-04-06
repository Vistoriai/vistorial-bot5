from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(
        {"status": "Online", "app": "VistoriAI"},
        status_code=200  # Isso evita o 404
    )

# Rota obrigatória para o Vercel
@app.get("/api/status")
async def status():
    return {"deploy": "success"}
