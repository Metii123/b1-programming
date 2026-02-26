import json
import os
from fastapi import APIRouter, HTTPException
from schema import User, UserCreate

router = APIRouter()

USERS_FILE = "users.txt"

def read_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        content = f.read().strip()
        return json.loads(content) if content else []

def write_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def get_next_id(users):
    return max((u["id"] for u in users), default=0) + 1


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = read_users()
    new_user = {"id": get_next_id(users), "name": user.name, "email": user.email}
    users.append(new_user)
    write_users(users)
    return new_user

@router.get("/", response_model=list[User])
def get_users():
    return read_users()

@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = read_users()
    return [u for u in users if q.lower() in u["name"].lower()]

@router.get("/{id}", response_model=User)
def get_user(id: int):
    users = read_users()
    for u in users:
        if u["id"] == id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{id}", response_model=User)
def update_user(id: int, user: UserCreate):
    users = read_users()
    for i, u in enumerate(users):
        if u["id"] == id:
            users[i] = {"id": id, "name": user.name, "email": user.email}
            write_users(users)
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    for i, u in enumerate(users):
        if u["id"] == id:
            users.pop(i)
            write_users(users)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")