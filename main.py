from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="TaskForge API",
    description="API REST para la gestión de tareas personales",
    version="1.0.0"
)

# Modelo de datos
class Task(BaseModel):
    title: str
    completed: bool = False

# Base de datos temporal
tasks = [
    {
        "id": 1,
        "title": "Estudiar Python",
        "completed": False
    },
    {
        "id": 2,
        "title": "Aprender FastAPI",
        "completed": True
    }
]

# GET - Listar tareas con filtro opcional
@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]


# POST - Crear tarea
@app.post("/tasks", status_code=201)
def create_task(task: Task):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task

# PUT - Actualizar tarea
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    for existing_task in tasks:

        if existing_task["id"] == task_id:

            existing_task["title"] = task.title
            existing_task["completed"] = task.completed

            return existing_task

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )

# DELETE - Eliminar tarea
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Tarea eliminada correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )
