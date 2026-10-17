# Machines API

Base path: `/api/v1/machines`

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
| `machine_code` | str |
| `name` | str |
| `work_center_id` | int |
| `make` | str |
| `commissioned_on` | date |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
