from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
    
)
get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def allBlogs(db:Session = Depends(database.get_db)):
  return blog.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session = Depends(database.get_db)):
   return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
   return blog.destroy(id,db)

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
  return blog.update(id,request,db)
   

@router.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def Show(id,response:Response,db:Session = Depends(get_db)):
  return blog.getById(id,db)
