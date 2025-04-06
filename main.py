from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Rota OBRIGATÓRIA para o Vercel
@app.get("/")
async def root():
    return JSONResponse({"status": "API Online", "app": "VistoriAI"})

# Rota de saúde exigida pelo Vercel
@app.get("/api/status")
async def health_check():
    return {"status": "ok", "version": "1.0"}

# Webhook para WhatsApp
@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    return JSONResponse({"received": True})
