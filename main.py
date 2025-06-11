from fastapi import FastAPI
import json,random
app = FastAPI()

with open("riddles.json", "r") as file:
    data = json.load(file)

@app.get("/")
async def get_riddle():
    riddle = random.choice(data)
    return riddle  