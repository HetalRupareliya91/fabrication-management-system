"""API tests for Routings."""
URL = "/api/v1/routings/"

PAYLOAD = {
    "part_number": "Sample part number",
    "sequence": 1,
    "operation": "Sample operation",
    "work_center_id": 1,
    "std_minutes": 10.5,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"part_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["part_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "part_number": "   "})
    assert response.status_code == 422
