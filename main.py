from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/listar")
def listar():
    f = open("contactos.txt", "r")
    return f.read()

@app.post("/alta/{nombre}/{telefono}")
def dar_alta(nombre: str, telefono: str):
    f = open("contactos.txt", "a")
    f.write("{\"nombre\":\"" + nombre + "\",\"telefono\":\"" + telefono + "\"}")
    f.close()
    return {"alta":"ok"}

@app.delete("/borrar")
def borrar():
    open("contactos.txt", "w").close()
    return {"borrado":"ok"}