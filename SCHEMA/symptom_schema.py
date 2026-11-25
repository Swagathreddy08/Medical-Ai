
from pydantic import BaseModel, ConfigDict, Field


class symtomsinfo(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    patient_id: str = Field(pattern=r"^[0-9a-fA-F]{24}$")
    symtoms: str = Field(min_length=5, max_length=2000)
    duration: str = Field(min_length=1, max_length=100)
    severity: str = Field(min_length=1, max_length=50)