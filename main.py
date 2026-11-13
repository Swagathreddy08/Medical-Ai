from fastapi import FastAPI
from routers.Prouter import path
app=FastAPI()
app.include_router(path,prefix="/patients")
@app.get("/")
def home():
    return{
  "application": "MediGuide AI",
  "version": "1.0.0",
  "status": "running",
  "message": "Healthcare assistance backend is active"
}