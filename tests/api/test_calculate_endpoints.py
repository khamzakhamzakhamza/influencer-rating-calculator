from fastapi.testclient import TestClient
from src.main import app
from tests.api.influencer_data import influencer

client = TestClient(app)

def test_calculate_rating_when_no_topic_provided_should_calculate_general_rating():
    # Arrange
    request = {
        "influencers": [ 
            influencer
        ]
    }

    # Act
    response = client.post("/calculate/", json=request)

    # Assert
    assert response.status_code == 200
    assert response.json()[0]["id"] == influencer["id"]
    assert response.json()[0]["rating"] == 0.75

def test_calculate_rating_when_topic_provided_should_calculate_topical_rating():
    # Arrange
    request = {
        "topic": "technology",
        "influencers": [
            influencer
        ]
    }

    # Act
    response = client.post("/calculate/", json=request)

    # Assert
    assert response.status_code == 200
    assert response.json()[0]["id"] == influencer["id"]
    assert response.json()[0]["rating"] == 0.75
