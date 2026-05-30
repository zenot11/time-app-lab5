from app import app

def test_time_route():
    client = app.test_client()
    response = client.get("/time")

    assert response.status_code == 200

    data = response.get_json()
    assert "time" in data
    assert isinstance(data["time"], int)
