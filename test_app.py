from app import app

def test_time_route():
    client = app.test_client()
    response = client.get("/time")

    assert response.status_code == 200

    data = response.get_json()
    assert "time" in data
    assert isinstance(data["time"], int)
    assert data["time"] > 0


def test_metrics_route():
    client = app.test_client()

    client.get("/time")
    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.get_json()
    assert "count" in data
    assert isinstance(data["count"], int)
    assert data["count"] >= 1
