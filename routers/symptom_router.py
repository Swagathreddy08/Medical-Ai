
from fastapi import APIRouter, HTTPException

from SCHEMA.symptom_schema import symtomsinfo

from model.symptom_model import (
    create_symptom,
    get_patient_symptoms
)

path2 = APIRouter()


# POST - SUBMIT SYMPTOMS
@path2.post("/symptoms/submit")
def symtoms_post(symtom: symtomsinfo):

    symtom_data = symtom.model_dump()

    try:
        symptom_id = create_symptom(symtom_data)

        return {
            "message": "Patient symptoms registered successfully",
            "patient_id": symtom_data["patient_id"],
            "symptom_id": symptom_id,
            "symptoms": symtom_data
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to register symptoms"
        )


@path2.get("/retrieve")
def symtoms_reterve(patient_id: str):

    p_history = get_patient_symptoms(patient_id)

    if not p_history:
        raise HTTPException(
            status_code=404,
            detail="No previous symptoms found"
        )

    return {
        "patient_id": patient_id,
        "total_records": len(p_history),
        "symptoms_history": p_history
    }
