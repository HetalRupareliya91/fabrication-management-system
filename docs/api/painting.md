# Painting API

Base path: `/api/v1/painting`

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
| `paint_system` | str |
| `dft_microns` | float |
| `coats` | int |
| `inspected` | bool |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
