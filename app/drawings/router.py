"""REST endpoints for Drawings."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import DrawingNotFound, DrawingValidationError
from .schemas import DrawingCreate, DrawingRead, DrawingUpdate

router = APIRouter(prefix="/drawings", tags=["Drawings"])


@router.get("/", response_model=list[DrawingRead])
def list_drawings(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=DrawingRead)
def get_drawings(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except DrawingNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=DrawingRead, status_code=status.HTTP_201_CREATED)
def create_drawings(payload: DrawingCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except DrawingValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=DrawingRead)
def update_drawings(item_id: int, payload: DrawingUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except DrawingNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DrawingValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_drawings(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except DrawingNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
