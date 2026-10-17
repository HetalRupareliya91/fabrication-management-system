# Invoices API

Base path: `/api/v1/invoices`

| Method | Path | Description |
|---|---|---|
| GET | `/` | List records (`skip`, `limit` query params) |
| GET | `/{id}` | Get one record |
| POST | `/` | Create a record |
| PATCH | `/{id}` | Partially update a record |
| DELETE | `/{id}` | Delete a record |

## Fields

| Field | Type |
|---|---|
| `invoice_number` | str |
| `sales_order_id` | int |
| `invoice_date` | date |
| `amount` | float |
| `paid` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
