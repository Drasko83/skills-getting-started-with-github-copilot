import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange
    # (No setup needed for this test)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"

    # Act - Sign up
    signup_response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert - Sign up
    assert signup_response.status_code in (200, 400)  # 400 if already signed up

    # Act - Unregister
    unregister_response = client.post(f"/activities/{activity}/unregister?email={email}")

    # Assert - Unregister
    assert unregister_response.status_code in (200, 404)  # 404 if not found
