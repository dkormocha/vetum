from fastapi import FastAPI
from app.database import engine, Base

# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Travel App API")

@app.get("/")
async def root():
    return {"status": "API running"}