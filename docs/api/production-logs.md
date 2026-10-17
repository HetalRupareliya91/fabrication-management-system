# Production Logs API

Base path: `/api/v1/production-logs`

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
| `operator_id` | int |
| `quantity_done` | int |
| `remarks` | str |
| `log_date` | date |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
