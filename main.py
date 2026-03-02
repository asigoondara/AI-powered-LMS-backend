from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Course, Enrollment

app = FastAPI(title="AI-Powered LMS")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to your AI-Powered LMS!"}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

from fastapi import Query
from ai_client import get_ai_response

@app.get("/ai/recommendations/")
def course_recommendations(user_name: str = Query(...)):
    prompt = f"Suggest 3 courses for a student named {user_name} based on their interests."
    ai_result = get_ai_response(prompt)
    return {"recommendations": ai_result}

@app.get("/ai/quiz/")
def generate_quiz(course_title: str = Query(...)):
    prompt = f"Generate a 5-question quiz for the course titled '{course_title}'."
    ai_result = get_ai_response(prompt)
    return {"quiz": ai_result}
