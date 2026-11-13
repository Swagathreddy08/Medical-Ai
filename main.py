from fastapi import FastAPI
from database.connection import check_database_connection
from routers.Prouter import path
app=FastAPI()
app.include_router(path,prefix="/patients")
@app.on_event("startup")
def startup_event():
    check_database_connection()

@app.get("/")
def home():
    return{
  "application": "MediGuide AI",
  "version": "1.0.0",
  "status": "running",
  "message": "Healthcare assistance backend is active"
}