"""REST endpoints for Non-Conformance Reports."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import NonConformanceNotFound, NonConformanceValidationError
from .schemas import NonConformanceCreate, NonConformanceRead, NonConformanceUpdate

router = APIRouter(prefix="/ncr", tags=["Non-Conformance Reports"])


@router.get("/", response_model=list[NonConformanceRead])
def list_ncr(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=NonConformanceRead)
def get_ncr(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except NonConformanceNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=NonConformanceRead, status_code=status.HTTP_201_CREATED)
def create_ncr(payload: NonConformanceCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except NonConformanceValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=NonConformanceRead)
def update_ncr(item_id: int, payload: NonConformanceUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except NonConformanceNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except NonConformanceValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_ncr(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except NonConformanceNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
