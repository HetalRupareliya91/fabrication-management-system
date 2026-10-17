# Sales Orders API

Base path: `/api/v1/sales-orders`

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
| `so_number` | str |
| `customer_id` | int |
| `order_date` | date |
| `delivery_date` | date |
| `status` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
