from typing import Union 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



memories = [
    {'id': 1, "title": "Vacation in Italty", "description": "Beautiful beaches and the best food"},
    {'id': 2, "title": "Solo trip to Budapest", "description": "Beatiful modern and historic city"}
]    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/memories/")
def get_memories():
    return memories

@app.get("/memories/{memory_id}")
def get_memory(memory_id: int):
    for memory in memories:
        if memory["id"] == memory_id:
            return memory
    return {"error": "Memory not found"}

@app.post("/memories/")
def create_memory(title: str, description: str):
    new_memory = {
        "id": len(memories) + 1,
        "title": title,
        "description": description
    }
    memories.append(new_memory)
    return new_memory
    