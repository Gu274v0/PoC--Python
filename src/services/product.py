from src.models import ProductModel
from pydantic import parse_obj_as
from src.db import products
from bson import ObjectId
from typing import List


class ProductService:
    def get_all():
        return parse_obj_as(List[ProductModel], list(products.find()))

    def get_one(id: str):
        item = None
        try:
            item = ProductModel.parse_obj(
                products.find_one({"_id": ObjectId(id)}))
        finally:
            return item

    def add(model: ProductModel):
        resp = None
        try:
            resp = products.insert_one({
                "name": model.name,
                "value": model.value,
                "image": model.image
            })
        finally:
            return resp != None and resp.inserted_id != None

    def update(id: str, model: ProductModel):
        resp = None
        try:
            resp = products.update_one({"_id": ObjectId(id)}, {"$set": {
                "name": model.name,
                "value": model.value,
                "image": model.image
            }})
        finally:
            return resp != None and resp.modified_count == 1

    def delete(id: str):
        resp = None
        try:
            resp = products.delete_one({"_id": ObjectId(id)})
        finally:
            return resp != None and resp.deleted_count == 1
