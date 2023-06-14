from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from ..import models
from ..hashing import Hash

def create(request,db:Session):
    
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def getAll(db:Session):
     Users= db.query(models.User).all()
     return Users
 
def getById(id,db:Session):
      usersdata = db.query(models.User).filter(models.User.id==id).first()
      return usersdata
