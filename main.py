
from fastapi import FastAPI

from routers.Prouter import patient_router
from routers.symptom_router import symptom_router

app = FastAPI(
    title="MediGuide AI",
    description="AI-powered healthcare assistance backend",
    version="1.0.0",
)

app.include_router(patient_router)
app.include_router(symptom_router)


@app.get("/")
def home():
    return {
        "application": "MediGuide AI",
        "status": "running",
    }
