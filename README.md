# MediGuide AI

A small FastAPI and MongoDB backend for patient profiles and symptom history.

## What works

- Create, view, update, and delete patient profiles.
- Submit symptoms for an existing patient.
- Retrieve a patient's symptom history.
- Validate request data and report common database errors.

AI and emergency-triage modules are placeholders and are not connected to the API yet.

## Run locally

Requirements: Python 3.10+ and a MongoDB connection string.

```bash
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and set:

```env
MONGODB_URL=your_mongodb_connection_string
```

Keep your real connection string private. Start the server with:

```bash
uvicorn main:app --reload
```

API documentation is available at <http://127.0.0.1:8000/docs>.

## API routes

| Method | Route | Purpose |
|---|---|---|
| `POST` | `/create` | Create a patient (`name`, `age`, `phone`, `address`) |
| `GET` | `/profile/{patient_id}` | Get a patient profile |
| `PATCH` | `/profile/{patient_id}` | Update a patient's `phone` or `address` |
| `DELETE` | `/delete/{patient_id}` | Delete a patient |
| `POST` | `/symptoms/submit` | Save symptoms (`patient_id`, `symtoms`, `duration`, `severity`) |
| `GET` | `/retrieve?patient_id={id}` | Get a patient's symptom history |

## Project files

```text
main.py                 FastAPI application
routers/                Patient and symptom endpoints
SCHEMA/                 Request validation
model/                  MongoDB symptom operations
database/connection.py  MongoDB connection
AI/                     Unfinished placeholders
```

## Next steps

- Add reviewed emergency warning rules and safety tests.
- Connect the AI modules only after their behavior is defined and reviewed.
- Add authentication before exposing patient data outside local development.

This project is not a medical device and does not provide diagnoses or treatment. Seek professional help for medical concerns or emergencies.
