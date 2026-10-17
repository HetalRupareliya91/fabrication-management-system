"""REST endpoints for Purchase Orders."""
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from . import service
from .exceptions import PurchaseOrderNotFound, PurchaseOrderValidationError
from .schemas import PurchaseOrderCreate, PurchaseOrderRead, PurchaseOrderUpdate

router = APIRouter(prefix="/purchase-orders", tags=["Purchase Orders"])


@router.get("/", response_model=list[PurchaseOrderRead])
def list_purchase_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return service.list_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=PurchaseOrderRead)
def get_purchase_orders(item_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_item(db, item_id)
    except PurchaseOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/", response_model=PurchaseOrderRead, status_code=status.HTTP_201_CREATED)
def create_purchase_orders(payload: PurchaseOrderCreate, db: Session = Depends(get_db)):
    try:
        return service.create_item(db, payload)
    except PurchaseOrderValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.patch("/{item_id}", response_model=PurchaseOrderRead)
def update_purchase_orders(item_id: int, payload: PurchaseOrderUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_item(db, item_id, payload)
    except PurchaseOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except PurchaseOrderValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.delete("/{item_id}", status_code=204, response_class=Response)
def delete_purchase_orders(item_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        service.delete_item(db, item_id)
    except PurchaseOrderNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return Response(status_code=204)
