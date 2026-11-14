
from database.connection import symptoms_collection
def create_symptom(symptom_data: dict):

    result = symptoms_collection.insert_one(symptom_data)

    return str(result.inserted_id)

def get_patient_symptoms(patient_id: str):

    p_history = list(
        symptoms_collection.find(
            {"patient_id": patient_id}
        )
    )

    for record in p_history:
        record["_id"] = str(record["_id"])

    return p_history
