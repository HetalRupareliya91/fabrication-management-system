"""API tests for Dispatch."""
URL = "/api/v1/dispatch/"

PAYLOAD = {
    "dispatch_number": "Sample dispatch number",
    "sales_order_id": 1,
    "vehicle_number": "Sample vehicle number",
    "dispatch_date": "2026-01-15",
    "weight_kg": 10.5,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"dispatch_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["dispatch_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "dispatch_number": "   "})
    assert response.status_code == 422
