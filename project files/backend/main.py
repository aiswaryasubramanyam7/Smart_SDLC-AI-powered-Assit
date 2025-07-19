from fastapi import FastAPI
from pydantic import BaseModel
from backend.watsonx_integration import ask_watsonx

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str
    task: str

@app.post("/ask/")
def ask_model(data: PromptInput):
    model_map = {
        "requirement": "granite-13b-chat-v1",
        "code": "granite-20b-code-instruct",
        "test": "granite-20b-code-instruct",
        "bugfix": "granite-20b-code-instruct",
        "docs": "granite-13b-chat-v1"
    }
    model_id = model_map.get(data.task, "granite-13b-chat-v1")
    result = ask_watsonx(data.prompt, model_id)
    return {"response": result}
