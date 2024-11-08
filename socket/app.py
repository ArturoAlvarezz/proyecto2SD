from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import json

data_usuarios = [
	{
        "usuario": "Augusto",
        "password": "1234",
        "tipo": "medico",
        "tipo_admin": None
    },
    {
        "usuario": "Paulo",
        "password": "1234",
        "tipo": "administrativo",
        "tipo_admin": "auxiliar"
    },
    {
        "usuario": "Jordan",
        "password": "1234",
        "tipo": "administrativo",
        "tipo_admin": "pabellon"
    },
    {
        "usuario": "Lorena",
        "password": "1234",
        "tipo": "medico",
        "tipo_admin": None
    },
    {
        "usuario": "Elver",
        "password": "1234",
        "tipo": "administrativo",
        "tipo_admin": "examenes"
    }
]

app = FastAPI()

class User(BaseModel):
  usuario: str
  password: str
  tipo: str
  tipo_admin: Optional[str] = None

class UserLogin(BaseModel):
  usuario: str
  password: str

@app.post("/crear-usuario")
async def crear_usuario(data: User):
  print("data", data.dict())
  if data.usuario in data_usuarios:
    return JSONResponse(status_code=400, content={"message": "Usuario ya existe"})
  elif data.tipo not in ["medico", "administrativo"]:
    return JSONResponse(status_code=400, content={"message": "Tipo de usuario no válido"})
  elif data.tipo == "administrativo" and data.tipo_admin not in ["auxiliar", "pabellon", "examenes", "admision"]:
    return JSONResponse(status_code=400, content={"message": "Tipo de administrativo no válido"})
  return JSONResponse(status_code=201, content={"message": "Usuario creado"})

@app.post("/login")
async def login(data: UserLogin):
  print("data", data.dict())
  for usuario in data_usuarios:
    if usuario["usuario"] == data.usuario and usuario["password"] == data.password:
      return JSONResponse(status_code=200, content={json.dumps(data_usuarios)})
  return JSONResponse(status_code=400, content={"message": "Usuario no encontrado"})

@app.get("/")
async def root():
  return {"message": "Socket Server is running"}
