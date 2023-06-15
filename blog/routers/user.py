from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user
router = APIRouter(
    prefix="/user",
    tags=['User']
    
)
get_db = database.get_db

@router.post('/')
def create_user(request:schemas.User,db:Session = Depends(get_db)):
      user.create(request,db)

@router.get('/AllUser',status_code=200)
def getAllUser(db:Session = Depends(get_db)):
  return user.getAll(db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id,db:Session=Depends(get_db)):
   return user.getById(id,db)
