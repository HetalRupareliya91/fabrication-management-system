"""API tests for Customers."""
URL = "/api/v1/customers/"

PAYLOAD = {
    "name": "Sample name",
    "gstin": "Sample gstin",
    "email": "Sample email",
    "phone": "Sample phone",
    "city": "Sample city",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"name": "Updated value"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "name": "   "})
    assert response.status_code == 422
