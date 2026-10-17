# Customers API

Base path: `/api/v1/customers`

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
| `name` | str |
| `gstin` | str |
| `email` | str |
| `phone` | str |
| `city` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
