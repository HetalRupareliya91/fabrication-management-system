"""API tests for Job Orders."""
URL = "/api/v1/job-orders/"

PAYLOAD = {
    "job_number": "Sample job number",
    "sales_order_id": 1,
    "part_number": "Sample part number",
    "quantity": 1,
    "status": "Sample status",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"job_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["job_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "job_number": "   "})
    assert response.status_code == 422
