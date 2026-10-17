# Drawings API

Base path: `/api/v1/drawings`

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
| `drawing_number` | str |
| `revision` | str |
| `title` | str |
| `approved` | bool |
| `customer_id` | int |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
