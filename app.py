from fastapi import FastAPI

app = FastAPI()

@summary_route := app.get("/")
def read_root():
    return {"message": "Task Manager API is running smoothly!"}

@app.get("/health")
def health_check():
    return {"status": "up", "database": "disconnected"}

@app.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "Review Kubernetes lab", "completed": False}]
