"""API tests for Work Centers."""
URL = "/api/v1/work-centers/"

PAYLOAD = {
    "code": "Sample code",
    "name": "Sample name",
    "capacity_hours": 10.5,
    "cost_per_hour": 10.5,
    "is_active": True,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"code": "Updated value"})
    assert response.status_code == 200
    assert response.json()["code"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "code": "   "})
    assert response.status_code == 422
