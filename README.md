"# Medical-Ai" 
# 🏥 MediGuide AI
### Intelligent Patient Assistance & Doctor Discovery System

**MediGuide AI** is an AI-powered healthcare assistance and doctor discovery backend application built using Python, FastAPI, and MongoDB.

The platform allows patients to describe their symptoms in natural language, receive preliminary health guidance based on approved medical information, identify potential emergency warning signs, and discover suitable doctors based on specialization and location.

The project combines **AI integration, backend engineering, database management, and intelligent automation** to demonstrate how modern healthcare assistance systems can be designed.

> **Project Status:** 🚧 Under Development

---

## 🎯 Project Vision

The primary goal of MediGuide AI is to simplify the initial healthcare assistance process by connecting patients with relevant medical guidance and healthcare professionals.

Instead of relying on a simple chatbot, the system follows a structured backend workflow involving input validation, rule-based safety checks, AI assistance, and doctor discovery.

### Example Interaction

**Patient:**
"I've had a headache and fever since yesterday."

**MediGuide AI:**
"I can help you understand the next steps. First, I need to ask a few questions about your symptoms and check for warning signs."

Based on the patient's responses, the system will:

- Validate the submitted information.
- Check for potential emergency warning signs.
- Ask relevant follow-up questions.
- Retrieve approved preliminary precautions.
- Suggest appropriate medical attention.
- Help discover suitable doctors.

---

## ✨ Core Features

The application is planned around eight major modules.

### 1. Patient Input System
- Accept symptoms in natural language.
- Collect symptom duration and severity.
- Capture relevant patient information.
- Support structured patient submissions.

### 2. Request Validation Engine
- Validate healthcare-related requests.
- Reject irrelevant or empty inputs.
- Identify missing information.
- Request clarification when necessary.

### 3. Medical Safety & Triage Engine
- Identify potential emergency warning signs.
- Apply deterministic safety rules.
- Prioritize emergency escalation.
- Provide urgency-based guidance.

### 4. AI Assistance Agent
- Understand natural-language symptom descriptions.
- Ask relevant follow-up questions.
- Generate understandable responses.
- Use approved medical information as its knowledge source.
- Apply safety restrictions to AI-generated responses.

### 5. Nearby Doctor Discovery
- Search doctors by specialization.
- Filter doctors by location.
- Discover nearby clinics.
- Support distance-based searches.

### 6. Doctor Availability
- Maintain doctor schedules.
- Retrieve available appointment slots.
- Verify availability before booking.
- Prevent duplicate appointment bookings.

### 7. Patient History
- Store symptom sessions.
- Maintain patient interaction history.
- Retrieve previous submissions.
- Track appointment information.

### 8. Monitoring & Administration
- Manage doctor information.
- Maintain approved medical guidelines.
- Monitor system activities.
- Maintain audit logs.

---

## 🧠 System Architecture

MediGuide AI follows a layered decision-making architecture.

```text
              PATIENT INPUT
                    |
                    v
           INPUT VALIDATION
                    |
                    v
          MEDICAL SAFETY ENGINE
                    |
             +------+------+
             |             |
          Emergency     Non-Emergency
             |             |
             v             v
       Immediate       AI ASSISTANCE
       Escalation           |
                           v
                  APPROVED GUIDELINES
                           |
                           v
                    DOCTOR DISCOVERY
                           |
                           v
                  APPOINTMENT CHECK
                           |
                           v
                   PATIENT RESPONSE
```

### Three Independent Processing Layers

| Layer | Responsibility |
|---|---|
| Validation Layer | Checks input quality and relevance |
| Safety Layer | Identifies emergency warning signs using predefined rules |
| AI Layer | Understands symptoms and communicates approved guidance |

**Important:** The AI model does not independently diagnose patients or override emergency safety rules. Emergency escalation must happen without waiting for an AI response.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API development |
| MongoDB | NoSQL database |
| PyMongo | MongoDB integration |
| Pydantic | Request and response validation |
| Gemini / OpenAI API | AI integration |
| Geocoding / Maps API | Location-based doctor discovery |
| JWT / OAuth2 | Authentication and authorization |
| Pytest | Backend testing |
| Docker | Application containerization |

### Advanced Concepts

The project will progressively introduce:

- Asynchronous programming
- MongoDB indexing and aggregation
- Geospatial queries
- AI structured outputs
- Function calling and tool integration
- Retrieval-Augmented Generation (RAG)
- Background tasks
- API security and rate limiting

---

## 🗄️ MongoDB Database Architecture

The application will use separate collections to maintain structured and manageable data.

| Collection | Responsibility |
|---|---|
| `patients` | Patient accounts and profiles |
| `symptom_sessions` | Submitted symptoms and patient sessions |
| `medical_guidelines` | Approved medical precautions |
| `doctors` | Doctor profiles and specialties |
| `clinics` | Hospital and clinic information |
| `doctor_availability` | Doctor appointment slots |
| `appointments` | Appointment records |
| `agent_interactions` | AI questions and responses |
| `audit_logs` | Important system activities |

### Database Relationships

- One patient can have multiple symptom sessions.
- One symptom session can have multiple AI interactions.
- One doctor can have multiple appointment slots.
- One appointment is associated with a patient and a doctor.
- Medical guidelines can be retrieved by relevant symptoms or categories.

The database design will progressively incorporate MongoDB references, embedded documents, indexes, and aggregation pipelines.

---

## 📁 Project Structure

The application follows a modular FastAPI architecture.

```text
mediguide-ai/
│
├── .venv/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── app/
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   │
│   ├── schemas/
│   │   ├── patient.py
│   │   ├── symptoms.py
│   │   └── doctor.py
│   │
│   ├── routers/
│   │   ├── patient.py
│   │   ├── symptoms.py
│   │   ├── doctors.py
│   │   └── appointments.py
│   │
│   ├── services/
│   │   ├── validation.py
│   │   ├── triage.py
│   │   ├── doctor_service.py
│   │   └── availability.py
│   │
│   ├── agents/
│   │   ├── medical_agent.py
│   │   ├── prompts.py
│   │   └── safety_guard.py
│   │
│   └── utils/
│       └── location.py
│
└── tests/
    ├── test_patients.py
    ├── test_symptoms.py
    └── test_triage.py
```

### Architectural Responsibilities

- **Models:** Represent database entities and persistence structure.
- **Schemas:** Validate incoming requests and outgoing responses.
- **Routers:** Handle HTTP requests and API endpoints.
- **Services:** Implement application business logic.
- **Agents:** Handle AI interactions and controlled tool execution.
- **Config:** Manage application settings and database connections.
- **Tests:** Verify application functionality and safety rules.

---

## 🚀 Development Roadmap

The project is being developed incrementally, with each module tested before proceeding to the next.

### Phase 1 — Backend Foundation
- [x] Project setup and virtual environment
- [x] FastAPI application structure
- [x] MongoDB connection
- [x] Pydantic schema fundamentals
- [x] Patient API development

### Phase 2 — Patient Symptom System
- [x] Symptom submission endpoint
- [x] Input validation
- [x] Store symptom sessions
- [x] Retrieve patient history
- [x] Error handling

### Phase 3 — Medical Safety Engine
- [ ] Rule-based emergency detection
- [ ] Emergency warning responses
- [ ] Approved medical precautions
- [ ] Urgency escalation
- [ ] Safety testing

### Phase 4 — AI Integration
- [ ] LLM API integration
- [ ] System prompt engineering
- [ ] Structured AI responses
- [ ] Follow-up questions
- [ ] Function calling
- [ ] Grounded medical responses

### Phase 5 — Doctor Discovery
- [ ] Doctor profiles
- [ ] Specialty-based filtering
- [ ] Clinic discovery
- [ ] Location-based searches
- [ ] Distance calculations

### Phase 6 — Availability & Appointments
- [ ] Doctor schedule management
- [ ] Appointment slot verification
- [ ] Appointment creation
- [ ] Double-booking prevention
- [ ] Appointment cancellation

### Phase 7 — Advanced AI Agent
- [ ] AI tool calling
- [ ] Retrieval-Augmented Generation
- [ ] Medical knowledge retrieval
- [ ] Multi-step agent workflows
- [ ] Conversation management
- [ ] AI response evaluation

### Phase 8 — Production Readiness
- [ ] Authentication and authorization
- [ ] Rate limiting
- [ ] Logging and monitoring
- [ ] Automated testing
- [ ] Docker integration
- [ ] Deployment
- [ ] Privacy and security review

---

## 🔐 Security & Medical Safety

Healthcare information requires special protection.

MediGuide AI aims to incorporate:

- Secure patient data storage.
- Authentication and authorization.
- Environment-based secret management.
- Restricted access to patient information.
- Appropriate consent mechanisms.
- Data encryption in transit and at rest.
- Audit logging.
- Data retention and deletion policies.
- Applicable Indian data-protection requirements.

### Medical Disclaimer

MediGuide AI is an educational and healthcare assistance project. It is not a substitute for professional medical diagnosis, treatment, or emergency services.

AI-generated information must not be treated as a medical diagnosis. Emergency symptoms require immediate professional medical attention.

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- MongoDB
- Git
- Code editor (VS Code recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mediguide-ai.git
```

### 2. Navigate to the Project

```bash
cd mediguide-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=mediguide
AI_API_KEY=your_ai_api_key
```

Never commit actual API keys, database credentials, or sensitive patient information to GitHub.

### 7. Run the Application

```bash
uvicorn main:app --reload
```

### 8. Explore API Documentation

Open the following URL after starting the application:

```text
http://127.0.0.1:8000/docs
```

---

## 🎓 Learning Objectives

This project is designed to demonstrate practical backend engineering skills through a real-world application.

By developing MediGuide AI, the following concepts will be explored:

- Designing scalable REST APIs.
- Building modular FastAPI applications.
- Managing MongoDB databases professionally.
- Implementing request validation and error handling.
- Integrating third-party APIs.
- Building controlled AI agents.
- Implementing rule-based safety systems.
- Designing geospatial search functionality.
- Managing appointment scheduling.
- Testing and securing backend applications.

---

## 🌟 Project Highlights

**MediGuide AI is more than a basic AI chatbot.**

It combines:

- AI-powered natural-language interaction.
- Independent rule-based safety checks.
- Medical knowledge retrieval.
- MongoDB-backed patient history.
- Location-aware doctor discovery.
- Appointment availability management.
- Modular backend architecture.

The main objective is to explore how AI can be integrated into a structured backend system while maintaining control, reliability, and safety.

---

## 📌 Future Enhancements

Potential future improvements include:

- Multilingual patient interaction.
- Voice-based symptom submission.
- Medical document processing.
- Prescription and report organization.
- Patient notification services.
- Doctor-side dashboard.
- Healthcare provider integrations.

---

## 👨‍💻 Development Philosophy

This project is being built with a learning-first, engineering-focused approach.

Instead of simply connecting an AI API and creating a chatbot, the development focuses on understanding backend architecture, database design, API workflows, system validation, AI integration, and real-world application logic.

**Build the logic. Understand the architecture. Integrate AI responsibly.**

---

**MediGuide AI — Smarter Healthcare Assistance Through AI & Backend Engineering.**