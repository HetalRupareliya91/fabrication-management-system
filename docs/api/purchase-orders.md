# Purchase Orders API

Base path: `/api/v1/purchase-orders`

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
| `po_number` | str |
| `supplier_id` | int |
| `order_date` | date |
| `total_amount` | float |
| `status` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
