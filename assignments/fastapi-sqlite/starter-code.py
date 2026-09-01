from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="Persistent Task API")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    completed: bool = False


class TaskUpdate(BaseModel):
    completed: bool


Base.metadata.create_all(bind=engine)


# Task 2: Create POST /tasks and GET /tasks.


# Task 3: Create PATCH /tasks/{task_id}.


# Run with: uvicorn starter-code:app --reload
