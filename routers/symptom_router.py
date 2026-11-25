
import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pymongo.errors import PyMongoError

from SCHEMA.symptom_schema import symtomsinfo
from database.connection import patients_collection
from model.symptom_model import create_symptom, get_patient_symptoms

logger = logging.getLogger(__name__)
path2 = APIRouter()


@path2.post("/symptoms/submit")
def symtoms_post(symptoms: symtomsinfo):
    symptom_data = symptoms.model_dump()

    try:
        patient = patients_collection.find_one(
            {"_id": ObjectId(symptom_data["patient_id"])},
            {"_id": 1},
        )
        if patient is None:
            raise HTTPException(status_code=404, detail="Patient not found")

        symptom_id = create_symptom(symptom_data)
    except PyMongoError as exc:
        logger.exception("Unable to register patient symptoms")
        raise HTTPException(
            status_code=503,
            detail="Symptom service is temporarily unavailable",
        ) from exc

    return {
        "message": "Patient symptoms registered successfully",
        "patient_id": symptom_data["patient_id"],
        "symptom_id": symptom_id,
        "symptoms": symptom_data,
    }


@path2.get("/retrieve")
def symtoms_reterve(patient_id: str):
    if not ObjectId.is_valid(patient_id):
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    try:
        patient = patients_collection.find_one(
            {"_id": ObjectId(patient_id)},
            {"_id": 1},
        )
        if patient is None:
            raise HTTPException(status_code=404, detail="Patient not found")

        history = get_patient_symptoms(patient_id)
    except PyMongoError as exc:
        logger.exception("Unable to retrieve patient symptom history")
        raise HTTPException(
            status_code=503,
            detail="Symptom service is temporarily unavailable",
        ) from exc

    if not history:
        raise HTTPException(
            status_code=404,
            detail="No previous symptoms found"
        )

    return {
        "patient_id": patient_id,
        "total_records": len(history),
        "symptoms_history": history,
    }
