from fastapi import APIRouter, HTTPException
from typing import List
from schemas.todo import TodoSchema
from crud.todo import create_todo, get_all_todos, get_todo, update_todo, delete_todo

router = APIRouter()

@router.post("/todos/", response_model=TodoSchema)
def create_todo_route(todo: TodoSchema):
    return create_todo(todo)

@router.get("/todos/", response_model=List[TodoSchema])
def read_all_route():
    return get_all_todos()

@router.get("/todos/{todo_id}", response_model=TodoSchema)
def read_one_route(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoSchema)
def update_todo_route(todo_id: int, updated_todo: TodoSchema):
    todo = update_todo(todo_id, updated_todo)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}", response_model=TodoSchema)
def delete_todo_route(todo_id: int):
    todo = delete_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
