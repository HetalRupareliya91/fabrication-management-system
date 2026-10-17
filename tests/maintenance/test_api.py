"""API tests for Maintenance."""
URL = "/api/v1/maintenance/"

PAYLOAD = {
    "machine_id": 1,
    "maintenance_type": "Sample maintenance type",
    "scheduled_on": "2026-01-15",
    "completed": True,
    "remarks": "Sample remarks",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"maintenance_type": "Updated value"})
    assert response.status_code == 200
    assert response.json()["maintenance_type"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "maintenance_type": "   "})
    assert response.status_code == 422
