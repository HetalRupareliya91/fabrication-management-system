"""REST endpoints for Dispatch."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import DispatchNotFound, DispatchValidationError
from .schemas import DispatchCreate, DispatchRead, DispatchUpdate

router = APIRouter(prefix="/dispatch", tags=["Dispatch"])


@router.get("/", response_model=list[DispatchRead])
def list_dispatch(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=DispatchRead)
def get_dispatch(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except DispatchNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=DispatchRead, status_code=status.HTTP_201_CREATED)
def create_dispatch(payload: DispatchCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except DispatchValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=DispatchRead)
def update_dispatch(item_id: int, payload: DispatchUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except DispatchNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DispatchValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_dispatch(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except DispatchNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
