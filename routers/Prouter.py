from fastapi import APIRouter
from SCHEMA.pcreate_schema import pcreate
path=APIRouter()
@path.get("/profile")
async def root(patient):
    return {
    patient
    }

@path.post("/create")
async def create(patient: pcreate):
 return {
 "message": "Patient details received",
 "patient": patient.model_dump()
 }

