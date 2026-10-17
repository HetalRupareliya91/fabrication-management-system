# Bill of Materials API

Base path: `/api/v1/bom`

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
| `parent_part` | str |
| `component_code` | str |
| `quantity` | float |
| `unit` | str |
| `scrap_percent` | float |

Text fields must not be blank and numeric fields must not be negative (HTTP 422).
