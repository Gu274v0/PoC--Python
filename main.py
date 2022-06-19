from fastapi import FastAPI
from src.router import api_router

app = FastAPI(title="Python - PoC")

app.include_router(api_router)
