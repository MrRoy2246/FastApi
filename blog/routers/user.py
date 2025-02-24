from typing import List
from fastapi import APIRouter,Depends, HTTPException, Response,status
from .. import schemas,database,models
from sqlalchemy.orm import Session
from ..repository import user
from .. hashing import Hash

router =APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db =database.get_db


@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session =Depends(get_db)):
    return user.create(request,db)
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session =Depends(get_db)):
   return user.getUser(id,db)