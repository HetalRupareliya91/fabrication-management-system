# Non-Conformance Reports API

Base path: `/api/v1/ncr`

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
| `ncr_number` | str |
| `job_order_id` | int |
| `description` | str |
| `disposition` | str |
| `closed` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
