from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    completed: bool = False


class TaskUpdate(BaseModel):
    completed: bool


tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
]


# Task 1: Create GET /.


# Task 2: Create GET /tasks and POST /tasks.


# Task 3: Create PATCH /tasks/{task_id} and DELETE /tasks/{task_id}.


# Run with: uvicorn starter-code:app --reload
