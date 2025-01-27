from typing import List, Optional
from models.todo import Todo
from database.connection import todos

def create_todo(todo: Todo) -> Todo:
    todos.append(todo)
    return todo

def get_all_todos() -> List[Todo]:
    return todos

def get_todo(todo_id: int) -> Optional[Todo]:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

def update_todo(todo_id: int, updated_todo: Todo) -> Optional[Todo]:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    return None

def delete_todo(todo_id: int) -> Optional[Todo]:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(index)
    return None
