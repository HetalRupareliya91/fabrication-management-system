"""API tests for Job Costing."""
URL = "/api/v1/costing/"

PAYLOAD = {
    "job_order_id": 1,
    "currency": "Sample currency",
    "material_cost": 10.5,
    "labour_cost": 10.5,
    "total_cost": 10.5,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"currency": "Updated value"})
    assert response.status_code == 200
    assert response.json()["currency"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "currency": "   "})
    assert response.status_code == 422
