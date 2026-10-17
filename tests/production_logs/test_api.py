"""API tests for Production Logs."""
URL = "/api/v1/production-logs/"

PAYLOAD = {
    "job_order_id": 1,
    "operator_id": 1,
    "quantity_done": 1,
    "remarks": "Sample remarks",
    "log_date": "2026-01-15",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"remarks": "Updated value"})
    assert response.status_code == 200
    assert response.json()["remarks"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "remarks": "   "})
    assert response.status_code == 422
