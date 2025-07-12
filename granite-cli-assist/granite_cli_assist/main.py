import logging
from fastapi import FastAPI
from pydantic import BaseModel

from .generator import Generator
from .middleware import LoggingMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.add_middleware(LoggingMiddleware)

gen = Generator("ibm-granite/granite-7b-base")

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate(p: Prompt):
    return {"response": gen.generate(p.prompt)}

@app.get("/livez")
def livez():
    return {"status": "ok"}
