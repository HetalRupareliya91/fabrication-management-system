# Operators API

Base path: `/api/v1/operators`

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
| `employee_code` | str |
| `name` | str |
| `skill` | str |
| `certification` | str |
| `is_active` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
