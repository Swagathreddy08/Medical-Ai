
from fastapi import FastAPI
from routers.Prouter import path
from routers.symptom_router import path2

app = FastAPI(
    title="MediGuide AI",
    description="AI-powered healthcare assistance backend",
    version="1.0.0"
)

app.include_router(path)
app.include_router(path2)

@app.get("/")
def home():
    return {
        "application": "MediGuide AI",
        "status": "running"
    }
