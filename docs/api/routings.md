# Routings API

Base path: `/api/v1/routings`

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
| `part_number` | str |
| `sequence` | int |
| `operation` | str |
| `work_center_id` | int |
| `std_minutes` | float |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
