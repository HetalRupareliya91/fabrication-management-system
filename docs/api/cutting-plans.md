# Cutting Plans API

Base path: `/api/v1/cutting-plans`

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
| `plan_number` | str |
| `job_order_id` | int |
| `sheet_size` | str |
| `utilization_percent` | float |
| `status` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
