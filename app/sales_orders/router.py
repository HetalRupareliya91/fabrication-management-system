"""REST endpoints for Sales Orders."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import SalesOrderNotFound, SalesOrderValidationError
from .schemas import SalesOrderCreate, SalesOrderRead, SalesOrderUpdate

router = APIRouter(prefix="/sales-orders", tags=["Sales Orders"])


@router.get("/", response_model=list[SalesOrderRead])
def list_sales_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=SalesOrderRead)
def get_sales_orders(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except SalesOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=SalesOrderRead, status_code=status.HTTP_201_CREATED)
def create_sales_orders(payload: SalesOrderCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except SalesOrderValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=SalesOrderRead)
def update_sales_orders(item_id: int, payload: SalesOrderUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except SalesOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except SalesOrderValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_sales_orders(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except SalesOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
