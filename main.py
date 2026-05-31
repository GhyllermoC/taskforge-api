from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="TaskForge API",
    description="API REST para la gestión de tareas personales con subtareas",
    version="2.0.0"
)

# Nuevo modelo de datos (cambio MAJOR)
class SubTask(BaseModel):
    id: int
    title: str
    completed: bool = False

class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: int  # 1 = Alta, 2 = Media, 3 = Baja
    completed: bool = False
    subtasks: List[SubTask] = []

# Base de datos temporal
tasks: List[Task] = []

# GET - Listar tareas
@app.get("/tasks")
def get_tasks():
    return tasks

# POST - Crear tarea
@app.post("/tasks", status_code=201)
def create_task(task: Task):
    tasks.append(task)
    return task

# PUT - Actualizar tarea
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for i, existing_task in enumerate(tasks):
        if existing_task.id == task_id:
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# DELETE - Eliminar tarea
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for existing_task in tasks:
        if existing_task.id == task_id:
            tasks.remove(existing_task)
            return {"message": "Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# POST - Añadir subtarea a una tarea
@app.post("/tasks/{task_id}/subtasks", status_code=201)
def add_subtask(task_id: int, subtask: SubTask):
    for task in tasks:
        if task.id == task_id:
            task.subtasks.append(subtask)
            return subtask
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
