from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel


app = FastAPI()


users = []

class User(BaseModel):
    id: int
    username: str
    age: int

users: List[User] = []

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_users(username: Annotated[
        str,
        Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int,Path(ge=1, le=100, description="Enter User ID", example=1)],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    for user in users:
        if user.id == user.id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int,Path(ge=1, le=100, description="Enter User ID", example=1)]) -> str:
    user_to_delete = None
    for user in users:
        if user.id == user.id:
            user_to_delete = user
            break
    if user_to_delete:
        users.remove(user_to_delete)
        return user_to_delete
    raise HTTPException(status_code=404, detail="User was not found")
