"""API tests for Painting."""
URL = "/api/v1/painting/"

PAYLOAD = {
    "job_order_id": 1,
    "paint_system": "Sample paint system",
    "dft_microns": 10.5,
    "coats": 1,
    "inspected": True,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"paint_system": "Updated value"})
    assert response.status_code == 200
    assert response.json()["paint_system"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "paint_system": "   "})
    assert response.status_code == 422
