import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db

client = TestClient(app)

def test_create_bookmark(client):
    response = client.post(
        "/shorten/",
        json={"url": "https://example.com", "title": "Test"}
    )
    assert response.status_code == 200
    assert "slug" in response.json()

def test_get_bookmark(client):
    response = client.get("/bookmarks/1")
    assert response.status_code in [200, 404]

def test_analytics(client):
    response = client.get("/analytics/")
    assert response.status_code == 200
    assert "total_bookmarks" in response.json()

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Bookmark Manager API"}
