"""API tests for Materials."""
URL = "/api/v1/materials/"

PAYLOAD = {
    "code": "Sample code",
    "description": "Sample description",
    "grade": "Sample grade",
    "thickness_mm": 10.5,
    "unit": "Sample unit",
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
