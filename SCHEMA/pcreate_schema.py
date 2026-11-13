
from pydantic import BaseModel, Field


class pcreate(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0)
    phone: str = Field(min_length=10, max_length=15)
    address: str = Field(min_length=3)


class pupdate(BaseModel):
    phone: str | None = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    address: str | None = Field(
        default=None,
        min_length=3
    )
