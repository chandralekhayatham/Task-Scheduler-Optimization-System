from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task Scheduler Optimization System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Task Scheduler Optimization System API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/schedule")
def schedule():

    tasks = [
        {
            "task_id": "T1",
            "start": 0,
            "end": 2
        },
        {
            "task_id": "T2",
            "start": 2,
            "end": 5
        },
        {
            "task_id": "T3",
            "start": 5,
            "end": 7
        }
    ]

    metrics = {
        "total_tasks": 3,
        "total_duration": 7
    }

    return {
        "status": "success",
        "algorithm": "Greedy Scheduling",
        "tasks": tasks,
        "metrics": metrics
    }