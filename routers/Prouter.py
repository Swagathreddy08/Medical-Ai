from fastapi import APIRouter,HTTPException
from SCHEMA.pcreate_schema import *
from SCHEMA.symptom_schema import *
from database.connection import patients_collection
from bson import ObjectId
path=APIRouter()

@path.get("/profile/{patient_id}")
async   def get_patient(patient_id: str):
        if not ObjectId.is_valid(patient_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid patient ID"
            )
        patient = patients_collection.find_one({
            "_id": ObjectId(patient_id)
        })
        if patient is None:
            raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )
        patient["_id"] = str(patient["_id"])
        return patient

@path.post("/create")
async def create(patient: pcreate):
    patient_data = patient.model_dump()
    try:
        
        result = patients_collection.insert_one(dict(patient_data))
        return {
            "message": "Patient registered successfully",
            "patient_id": str(result.inserted_id),
            "patient": patient_data
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to register patient"
        )
    
@path.patch("/profile/{patient_id}")
def update_patient(patient_id: str, patient: pupdate):

    result = patients_collection.update_one(
        {"_id": ObjectId(patient_id)},
        {"$set": patient.model_dump()}
    )
    return {
        "message": "Patient updated successfully",
        "updated_data": patient.model_dump()
    }

@path.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    if not ObjectId.is_valid(patient_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid Patient ID"
        )

    result = patients_collection.delete_one(
        {"_id": ObjectId(patient_id)}
    )
    return {
        "message": "Patient deleted successfully",
        "patient_id": patient_id
    }
