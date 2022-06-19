from pydantic import Field, BaseModel as ModelBase


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return str(v)


class BaseModel(ModelBase):
    id: ObjectIdStr = Field(None, alias='_id')
