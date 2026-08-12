from app.app import app


def test_root_returns_hello_message():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello from Flask!"
