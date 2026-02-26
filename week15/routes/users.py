import json
import os
from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    user_id = store.save({"name": user.name, "email": user.email})
    return {"id": user_id, "name": user.name, "email": user.email}

@router.get("/", response_model=list[User])
def get_users():
    return store.load()

@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = store.load()
    return [u for u in users if q.lower() in u["name"].lower()]

@router.get("/{id}", response_model=User)
def get_user(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=User)
def update_user(id: int, user: UserCreate):
    updated = store.update_user(id, {"name": user.name, "email": user.email})
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{id}")
def delete_user(id: int):
    success = store.delete_user(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}