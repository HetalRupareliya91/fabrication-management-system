# Dispatch API

Base path: `/api/v1/dispatch`

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
| `dispatch_number` | str |
| `sales_order_id` | int |
| `vehicle_number` | str |
| `dispatch_date` | date |
| `weight_kg` | float |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
