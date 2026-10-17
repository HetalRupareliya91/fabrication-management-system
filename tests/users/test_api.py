"""API tests for Users."""
URL = "/api/v1/users/"

PAYLOAD = {
    "username": "Sample username",
    "email": "Sample email",
    "full_name": "Sample full name",
    "role": "Sample role",
    "is_active": True,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"username": "Updated value"})
    assert response.status_code == 200
    assert response.json()["username"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "username": "   "})
    assert response.status_code == 422
