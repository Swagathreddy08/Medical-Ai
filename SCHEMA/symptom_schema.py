
from pydantic import BaseModel, Field
class symtomsinfo(BaseModel):
    patient_id: str 
    symtoms: str = Field(min_length=5)
    duration: str 
    severity: str 