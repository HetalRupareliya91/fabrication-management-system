"""API tests for Non-Conformance Reports."""
URL = "/api/v1/ncr/"

PAYLOAD = {
    "ncr_number": "Sample ncr number",
    "job_order_id": 1,
    "description": "Sample description",
    "disposition": "Sample disposition",
    "closed": True,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"ncr_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["ncr_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "ncr_number": "   "})
    assert response.status_code == 422
