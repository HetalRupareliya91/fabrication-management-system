"""API tests for Inventory."""
URL = "/api/v1/inventory/"

PAYLOAD = {
    "material_code": "Sample material code",
    "location": "Sample location",
    "quantity": 10.5,
    "reorder_level": 10.5,
    "batch_no": "Sample batch no",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"material_code": "Updated value"})
    assert response.status_code == 200
    assert response.json()["material_code"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "material_code": "   "})
    assert response.status_code == 422
