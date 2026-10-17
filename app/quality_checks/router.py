"""REST endpoints for Quality Checks."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import QualityCheckNotFound, QualityCheckValidationError
from .schemas import QualityCheckCreate, QualityCheckRead, QualityCheckUpdate

router = APIRouter(prefix="/quality-checks", tags=["Quality Checks"])


@router.get("/", response_model=list[QualityCheckRead])
def list_quality_checks(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=QualityCheckRead)
def get_quality_checks(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except QualityCheckNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=QualityCheckRead, status_code=status.HTTP_201_CREATED)
def create_quality_checks(payload: QualityCheckCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except QualityCheckValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=QualityCheckRead)
def update_quality_checks(item_id: int, payload: QualityCheckUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except QualityCheckNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except QualityCheckValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_quality_checks(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except QualityCheckNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
