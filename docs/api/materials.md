# Materials API

Base path: `/api/v1/materials`

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
| `description` | str |
| `grade` | str |
| `thickness_mm` | float |
| `unit` | str |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
