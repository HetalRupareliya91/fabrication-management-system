"""REST endpoints for Shifts."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import ShiftNotFound, ShiftValidationError
from .schemas import ShiftCreate, ShiftRead, ShiftUpdate

router = APIRouter(prefix="/shifts", tags=["Shifts"])


@router.get("/", response_model=list[ShiftRead])
def list_shifts(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ShiftRead)
def get_shifts(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except ShiftNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=ShiftRead, status_code=status.HTTP_201_CREATED)
def create_shifts(payload: ShiftCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except ShiftValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=ShiftRead)
def update_shifts(item_id: int, payload: ShiftUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except ShiftNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ShiftValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_shifts(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except ShiftNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
