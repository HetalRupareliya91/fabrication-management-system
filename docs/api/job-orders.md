# Job Orders API

Base path: `/api/v1/job-orders`

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
| `job_number` | str |
| `sales_order_id` | int |
| `part_number` | str |
| `quantity` | int |
| `status` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
