"""REST endpoints for Welding Records."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import WeldingRecordNotFound, WeldingRecordValidationError
from .schemas import WeldingRecordCreate, WeldingRecordRead, WeldingRecordUpdate

router = APIRouter(prefix="/welding-records", tags=["Welding Records"])


@router.get("/", response_model=list[WeldingRecordRead])
def list_welding_records(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=WeldingRecordRead)
def get_welding_records(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except WeldingRecordNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=WeldingRecordRead, status_code=status.HTTP_201_CREATED)
def create_welding_records(payload: WeldingRecordCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except WeldingRecordValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=WeldingRecordRead)
def update_welding_records(item_id: int, payload: WeldingRecordUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except WeldingRecordNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except WeldingRecordValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_welding_records(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except WeldingRecordNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
