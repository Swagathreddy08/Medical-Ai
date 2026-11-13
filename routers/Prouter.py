from fastapi import APIRouter,HTTPException
from SCHEMA.pcreate_schema import pcreate
path=APIRouter()

pat=[]
@path.get("/profile/{name}")
async def root(name:str):
    for patient in pat:
        if patient["name"]==name:
            return{
                "Name":patient["name"],
                "Age":patient["age"],
                "city":patient["address"]
            }
    else:
         raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )  

@path.post("/create")
async def create(patient: pcreate):
    p = patient.model_dump()
    pat.append(p)

    return {
        "message": "Patient details received",
        "patient": p
    }

