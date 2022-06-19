from src.models import ResponseModel, ProductModel
from src.services import ProductService
from fastapi import APIRouter, Response
from typing import List

router = APIRouter()
service = ProductService


@router.get("/", response_model=List[ProductModel], name="Get all products", description="Get all products in list")
def get_all():
    return service.get_all()


@router.get("/{id}", response_model=ProductModel, name="Get one product by _id", description="Get one single product per his _id")
def get_one(id: str):
    return service.get_one(id)


@router.post("/", response_model=ResponseModel, name="Add product", description="Add one product to db")
def add(model: ProductModel):
    return ResponseModel(success=(service.add(model)))


@router.put("/{id}", response_model=ResponseModel, name="Update one product by _id", description="Get one single product per his _id and update him")
def edit(id: str, model: ProductModel):
    return ResponseModel(success=(service.update(id, model)))


@router.delete("/{id}", response_model=ResponseModel, name="Delete product", description="Get one single product per his _id and delete him")
def delete(id: str):
    return ResponseModel(success=(service.delete(id)))
