from pydantic import BaseModel


class ResponseModel(BaseModel):
    success: bool = False
