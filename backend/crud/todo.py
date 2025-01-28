from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.todo import Todo
from ..database.connection import SessionLocal, TodoDB

def create_todo(todo: Todo) -> Todo:
    db = SessionLocal()
    db_todo = TodoDB(title=todo.title, description=todo.description, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo

def get_all_todos() -> List[Todo]:
    db = SessionLocal()
    todos = db.query(TodoDB).all()
    db.close()
    return todos

def get_todo(todo_id: int) -> Optional[Todo]:
    db = SessionLocal()
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    db.close()
    return todo

def update_todo(todo_id: int, updated_todo: Todo) -> Optional[Todo]:
    db = SessionLocal()
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if todo:
        todo.title = updated_todo.title
        todo.description = updated_todo.description
        todo.completed = updated_todo.completed
        db.commit()
        db.refresh(todo)
    db.close()
    return todo

def delete_todo(todo_id: int) -> Optional[Todo]:
    db = SessionLocal()
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    db.close()
    return todo
