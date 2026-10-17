# Suppliers API

Base path: `/api/v1/suppliers`

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
| `contact_person` | str |
| `phone` | str |
| `rating` | int |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
