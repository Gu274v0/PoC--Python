from fastapi import APIRouter
from src.endpoints import productRouter

api_router = APIRouter()
api_router.include_router(productRouter, prefix="/product", tags=["Product"])
