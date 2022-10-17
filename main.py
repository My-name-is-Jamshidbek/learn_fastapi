from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def main():
    return {'win':'main','func':'main','creator':'t.me/mal_un'}
@app.get('/about')
async def about():
    return {'about':'Bu Jamshidbek Ollanazarovning birinchi fastapi loyihasi'}
@app.get("/component/{param}")
async def get_param(param: int):
    return {'param':{param}}
@app.get("/components/")
async def get_params(number: int, text: str, yourname: Optional[str]):
    return {'param1':number, 'text': text, 'yournme':yourname}
class Package(BaseModel):
    name: str
    token: str
    description: Optional[str] = None
@app.get("/package/")
async def make_package(package: Package):
    return {**package.dict()}
