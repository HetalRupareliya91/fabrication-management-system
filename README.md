# Fabrication Management System

A modular FastAPI + SQLAlchemy backend for running a fabrication shop: from
quotation and sales order through drawings, BOM, routing, job orders, cutting,
welding, painting, quality control, dispatch, invoicing and job costing.

## Modules

- **Users** - `/api/v1/users`
- **Customers** - `/api/v1/customers`
- **Suppliers** - `/api/v1/suppliers`
- **Materials** - `/api/v1/materials`
- **Inventory** - `/api/v1/inventory`
- **Purchase Orders** - `/api/v1/purchase-orders`
- **Quotations** - `/api/v1/quotations`
- **Sales Orders** - `/api/v1/sales-orders`
- **Drawings** - `/api/v1/drawings`
- **Bill of Materials** - `/api/v1/bom`
- **Work Centers** - `/api/v1/work-centers`
- **Machines** - `/api/v1/machines`
- **Routings** - `/api/v1/routings`
- **Job Orders** - `/api/v1/job-orders`
- **Cutting Plans** - `/api/v1/cutting-plans`
- **Welding Records** - `/api/v1/welding-records`
- **Painting** - `/api/v1/painting`
- **Operators** - `/api/v1/operators`
- **Shifts** - `/api/v1/shifts`
- **Production Logs** - `/api/v1/production-logs`
- **Quality Checks** - `/api/v1/quality-checks`
- **Non-Conformance Reports** - `/api/v1/ncr`
- **Maintenance** - `/api/v1/maintenance`
- **Dispatch** - `/api/v1/dispatch`
- **Invoices** - `/api/v1/invoices`
- **Job Costing** - `/api/v1/costing`

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs for the interactive API.

## Tests

```bash
pytest -q
```

## Docker

```bash
docker build -t fabrication-system .
docker run -p 8000:8000 fabrication-system
```

## Configuration

| Variable | Default |
|---|---|
| `APP_NAME` | Fabrication Management System |
| `DATABASE_URL` | sqlite:///./fabrication.db |
