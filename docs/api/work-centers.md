# Work Centers API

Base path: `/api/v1/work-centers`

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
| `code` | str |
| `name` | str |
| `capacity_hours` | float |
| `cost_per_hour` | float |
| `is_active` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
