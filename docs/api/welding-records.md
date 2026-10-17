# Welding Records API

Base path: `/api/v1/welding-records`

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
| `welder_id` | int |
| `wps_number` | str |
| `joint_id` | str |
| `passed` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
