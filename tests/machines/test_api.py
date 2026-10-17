"""API tests for Machines."""
URL = "/api/v1/machines/"

PAYLOAD = {
    "machine_code": "Sample machine code",
    "name": "Sample name",
    "work_center_id": 1,
    "make": "Sample make",
    "commissioned_on": "2026-01-15",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"machine_code": "Updated value"})
    assert response.status_code == 200
    assert response.json()["machine_code"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "machine_code": "   "})
    assert response.status_code == 422
