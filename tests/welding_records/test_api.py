"""API tests for Welding Records."""
URL = "/api/v1/welding-records/"

PAYLOAD = {
    "job_order_id": 1,
    "welder_id": 1,
    "wps_number": "Sample wps number",
    "joint_id": "Sample joint id",
    "passed": True,
}


def test_crud_flow(client):
    response = client.post(URL, json=PAYLOAD)
    assert response.status_code == 201
    item_id = response.json()["id"]

    assert client.get(f"{URL}{item_id}").status_code == 200
    assert len(client.get(URL).json()) == 1

    response = client.patch(f"{URL}{item_id}", json={"wps_number": "Updated value"})
    assert response.status_code == 200
    assert response.json()["wps_number"] == "Updated value"

    assert client.delete(f"{URL}{item_id}").status_code == 204
    assert client.get(f"{URL}{item_id}").status_code == 404


def test_blank_text_returns_422(client):
    response = client.post(URL, json={**PAYLOAD, "wps_number": "   "})
    assert response.status_code == 422
