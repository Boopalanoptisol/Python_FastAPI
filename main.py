from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog List'}
@app.get('/blog')
def abc(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
         return{'data':f'{limit} published blog Check'}
    else:
         return{'data':f'{limit}blog Check'}
    print(limit,'limit')
    return{'data':f'{limit}blog Check'}

@app.get('/blog/{id}')

def show(id='2'):
    return{'data':id}


class Blog(BaseModel):
   title:str
   body:str
   publishedAt:Optional[bool]
@app.post('/blog')

def create_blog(request:Blog):
    return {'data':f"Blog is created with {request.title}"}
  
