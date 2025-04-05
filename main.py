from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse({"status": "API Online - VistoriAI"})

# ESSA ROTA É OBRIGATÓRIA PARA O VERCEL
@app.get("/api/status")
async def vercel_check():
    return JSONResponse({"deploy": "success"})
