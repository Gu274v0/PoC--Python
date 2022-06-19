
from src.models.base import BaseModel


class ProductModel(BaseModel):
    name: str = None
    value: float = None
    image: str = None
