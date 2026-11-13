from fastapi import APIRouter,HTTPException
from SCHEMA.symptom_schema import *
from database.connection import symptoms_collection
from bson import ObjectId
path2=APIRouter()
@path2.post("/symptoms/submit")
def symtoms_post(symtom:symtomsinfo):
    symtom_data=symtom.model_dump()
    try:
        result = symptoms_collection.insert_one(dict(symtom_data))
        return {
            "message": "Patient registered successfully",
            "patient_id": str(result.inserted_id),
            "symtoms": symtom_data
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to register patient"
        )
@path2.get("/retreive")
def symtoms_reterve(patient_id: str):
        if not ObjectId.is_valid(patient_id):
            raise HTTPException(
                status_code=400,
                detail="Invalid patient ID"
            )
        p_history = list(symptoms_collection.find({"patient_id": patient_id}))

        if not p_history:
            raise HTTPException(
            status_code=404,
            detail="No previous symptoms found"
        )

        for record in p_history:
            record["_id"] = str(record["_id"])

        return {
        "patient_id": patient_id,
        "total_records": len(p_history),
        "symptoms_history": p_history
    }
