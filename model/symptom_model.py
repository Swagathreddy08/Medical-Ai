
from datetime import datetime, timezone

from database.connection import symptoms_collection


def create_symptom(symptom_data: dict) -> str:
    symptom_record = {
        **symptom_data,
        "created_at": datetime.now(timezone.utc),
    }
    result = symptoms_collection.insert_one(symptom_record)

    return str(result.inserted_id)


def get_patient_symptoms(patient_id: str) -> list[dict]:
    history = list(
        symptoms_collection.find(
            {"patient_id": patient_id}
        ).sort("created_at", -1)
    )

    for record in history:
        record["_id"] = str(record["_id"])

    return history
