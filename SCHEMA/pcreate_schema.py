
from pydantic import BaseModel, ConfigDict, Field, model_validator


class pcreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: str = Field(min_length=3)
    age: int = Field(gt=0)
    phone: str = Field(min_length=10, max_length=15)
    address: str = Field(min_length=3)


class pupdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    phone: str | None = Field(
        default=None,
        min_length=10,
        max_length=15
    )

    address: str | None = Field(
        default=None,
        min_length=3
    )

    @model_validator(mode="after")
    def require_update_fields(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")
        return self
