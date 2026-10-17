"""API tests for Drawings."""
URL = "/api/v1/drawings/"

PAYLOAD = {
    "drawing_number": "Sample drawing number",
    "revision": "Sample revision",
    "title": "Sample title",
    "approved": True,
    "customer_id": 1,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"drawing_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["drawing_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "drawing_number": "   "})
    assert response.status_code == 422
