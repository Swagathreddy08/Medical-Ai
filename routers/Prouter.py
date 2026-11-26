import logging

from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pymongo.errors import PyMongoError

from SCHEMA.pcreate_schema import pcreate, pupdate
from database.connection import patients_collection

logger = logging.getLogger(__name__)
patient_router = APIRouter()


@patient_router.get("/profile/{patient_id}")
def get_patient(patient_id: str):
    if not ObjectId.is_valid(patient_id):
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    try:
        patient = patients_collection.find_one({"_id": ObjectId(patient_id)})
    except PyMongoError as exc:
        logger.exception("Unable to retrieve patient profile")
        raise HTTPException(
            status_code=503,
            detail="Patient service is temporarily unavailable",
        ) from exc

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient["_id"] = str(patient["_id"])
    return patient


@patient_router.post("/create")
def create(patient: pcreate):
    patient_data = patient.model_dump()
    try:
        result = patients_collection.insert_one(patient_data)
    except PyMongoError as exc:
        logger.exception("Unable to register patient")
        raise HTTPException(
            status_code=503,
            detail="Patient service is temporarily unavailable",
        ) from exc

    return {
        "message": "Patient registered successfully",
        "patient_id": str(result.inserted_id),
        "patient": patient_data,
    }


@patient_router.patch("/profile/{patient_id}")
def update_patient(patient_id: str, patient: pupdate):
    if not ObjectId.is_valid(patient_id):
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    updated_data = patient.model_dump(exclude_unset=True)
    try:
        result = patients_collection.update_one(
            {"_id": ObjectId(patient_id)},
            {"$set": updated_data},
        )
    except PyMongoError as exc:
        logger.exception("Unable to update patient profile")
        raise HTTPException(
            status_code=503,
            detail="Patient service is temporarily unavailable",
        ) from exc

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {
        "message": "Patient updated successfully",
        "updated_data": updated_data,
    }


@patient_router.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    if not ObjectId.is_valid(patient_id):
        raise HTTPException(status_code=400, detail="Invalid patient ID")

    try:
        result = patients_collection.delete_one({"_id": ObjectId(patient_id)})
    except PyMongoError as exc:
        logger.exception("Unable to delete patient")
        raise HTTPException(
            status_code=503,
            detail="Patient service is temporarily unavailable",
        ) from exc

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {
        "message": "Patient deleted successfully",
        "patient_id": patient_id,
    }
