from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Query, Form, File
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
import service, models, schemas
from database import SessionLocal, engine
from middleware.application_middleware import default_dependency
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency),  ):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/user_id/')
async def get_users_user_id(request: Request, query: schemas.GetUsersUserIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency),  ):
    try:
        return await service.get_users_user_id(request, db, query.user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency),  ):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/user_id/')
async def put_users_user_id(request: Request, raw_data: schemas.PutUsersUserId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency),  ):
    try:
        return await service.put_users_user_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/user_id/')
async def delete_users_user_id(request: Request, query: schemas.DeleteUsersUserIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_users_user_id(request, db, query.user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

