from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from storage import users

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/users/login")
def login_user(user: User):
    for u in users:
        if u["username"] == user.username and u["password"] == user.password:
            return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# CREATE
@router.post("/users")
def register_user(user: User):
    for u in users:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append(user.dict())
    return {"message": "User registered successfully", "user": user}

# READ - all users
@router.get("/users")
def get_all_users():
    return {"users": users}

# READ - single user
@router.get("/users/{username}")
def get_user(username: str):
    for u in users:
        if u["username"] == username:
            return u
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE
@router.put("/users/{username}")
def update_user(username: str, updated_user: User):
    for u in users:
        if u["username"] == username:
            u.update(updated_user.dict())
            return {"message": "User updated", "user": u}
    raise HTTPException(status_code=404, detail="User not found")

# DELETE
@router.delete("/users/{username}")
def delete_user(username: str):
    for i, u in enumerate(users):
        if u["username"] == username:
            users.pop(i)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
