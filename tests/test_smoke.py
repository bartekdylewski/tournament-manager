def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Turnieje" in response.text


def test_static_bootstrap_served(client):
    assert client.get("/static/css/bootstrap.min.css").status_code == 200
