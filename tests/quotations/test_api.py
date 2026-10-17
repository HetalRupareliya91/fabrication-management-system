"""API tests for Quotations."""
URL = "/api/v1/quotations/"

PAYLOAD = {
    "quote_number": "Sample quote number",
    "customer_id": 1,
    "valid_until": "2026-01-15",
    "amount": 10.5,
    "status": "Sample status",
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"quote_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["quote_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "quote_number": "   "})
    assert response.status_code == 422
