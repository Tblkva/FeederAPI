from typing import Union

from fastapi import FastAPI
from FeederAPI.Characters.characters import Champions
app = FastAPI()


@app.get("/")
async def read_root():
    db = await Champions.load_from_url()
    return {'champ': db}