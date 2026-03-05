🌍 Travel Planner Web Application

A full-stack travel social application built with FastAPI that allows users to search other users with same/similar location and travel date, with secure authentication and multi-user support.

⸻

🚀 Features To Add:
	•	🔐 User registration and login (JWT authentication)
	•	👤 Multi-user support
	•	🗓️ Date-based filtering
	•	📦 RESTful API design
	•	🗄️ PostgreSQL database integration
	•	🔄 Database migrations with Alembic
	•	🐳 Docker support (optional)
	•	☁️ Cloud deployment ready (e.g., AWS EC2)

⸻

🏗️ Tech Stack

Backend
	•	FastAPI
	•	Uvicorn
	•	SQLAlchemy
	•	PostgreSQL
	•	Pydantic
	•	Alembic



📁 Project Structure

Vetum/
├── app/
│   ├── main.py           # FastAPI entry point
│   ├── api/              # API route definitions
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic layer
│   ├── db/               # Database configuration
│   └── core/             # Settings & security
├── alembic/              # Database migrations
├── tests/                # Unit and integration tests
├── requirements.txt
├── docker-compose.yml
└── README.md


⸻

🗄️ Database Setup

Run migrations:

alembic upgrade head


⸻

▶️ Running the Application

Development mode

uvicorn app.main:app --reload

Application will be available at:

http://127.0.0.1:8000

Interactive API documentation:
	•	Swagger UI → /docs
	•	ReDoc → /redoc



⸻

🔐 Authentication Flow
	1.	User registers
	2.	Password is securely hashed
	3.	User logs in
	4.	JWT access token is generated
	5.	Protected routes require Bearer token authentication

⸻

🧪 Running Tests

pytest



👨‍💻 Author

Dhiraj
