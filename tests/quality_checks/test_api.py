"""API tests for Quality Checks."""
URL = "/api/v1/quality-checks/"

PAYLOAD = {
    "job_order_id": 1,
    "stage": "Sample stage",
    "inspector": "Sample inspector",
    "result": "Sample result",
    "check_date": "2026-01-15",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"stage": "Updated value"})
    assert response.status_code == 200
    assert response.json()["stage"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "stage": "   "})
    assert response.status_code == 422
