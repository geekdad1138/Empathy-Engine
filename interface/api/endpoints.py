# interface/api/endpoints.py
from fastapi import FastAPI
from pydantic import BaseModel
from core.emotion import EmotionalCore

app = FastAPI(title="Empathy Engine API - Demo")
ec = EmotionalCore()

class TextIn(BaseModel):
    user_id: str
    text: str

@app.post("/analyze")
def analyze(payload: TextIn):
    vec = ec.rough_affect(payload.text)
    return {"user_id": payload.user_id, "affect": vec}
