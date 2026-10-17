"""API tests for Bill of Materials."""
URL = "/api/v1/bom/"

PAYLOAD = {
    "parent_part": "Sample parent part",
    "component_code": "Sample component code",
    "quantity": 10.5,
    "unit": "Sample unit",
    "scrap_percent": 10.5,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"parent_part": "Updated value"})
    assert response.status_code == 200
    assert response.json()["parent_part"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "parent_part": "   "})
    assert response.status_code == 422
