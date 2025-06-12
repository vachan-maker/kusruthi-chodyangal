from fastapi import FastAPI
import json,random
app = FastAPI()

with open("riddles.json", "r") as file:
    data = json.load(file)

@app.get("/")
async def get_all():
    return data

@app.get("/random")
async def get_riddle():
    return random.choice(data)

@app.get("/{id}")
async def get_riddle_id(id: int):
    for item in data:
        if (item["id"] == id):
            return item
    return {"error": "Riddle not found"}