from pydantic import BaseModel,Field

class pcreate(BaseModel):
        name:str=Field(min_length=3)
        age : int=Field(ge=1)
        phone_no :str=Field(min_length=10)
        address : str           