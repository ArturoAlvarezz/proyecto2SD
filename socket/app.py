from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
  nombre: str
  tipo: str
  tipo_admin: Optional[str] = None

@app.post("/crear-usuario")
async def crear_usuario(data: User):
  print("data", data.dict())
  return data

@app.get("/")
async def root():
  return {"message": "Socket Server is running"}
