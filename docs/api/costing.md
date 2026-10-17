# Job Costing API

Base path: `/api/v1/costing`

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
| `job_order_id` | int |
| `currency` | str |
| `material_cost` | float |
| `labour_cost` | float |
| `total_cost` | float |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
