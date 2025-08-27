from typing import List
from fastapi.testclient import TestClient
from pydantic import TypeAdapter
from src.domain.calculator.calculate_response import CalculateResponse
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
    adapter = TypeAdapter(List[CalculateResponse])
    parsed: List[CalculateResponse] = adapter.validate_python(response.json())
    first = parsed[0]
    assert first.id == influencer["id"]
    assert first.audience_size == 0.364
    assert first.audience_makeup == 0.506
    assert first.posts_per_week == 0.425
    assert first.engagement_per_audience == 0.026
    assert first.tone_of_voice == 1.0
    assert first.rating == 0.464

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
    adapter = TypeAdapter(List[CalculateResponse])
    parsed: List[CalculateResponse] = adapter.validate_python(response.json())
    first = parsed[0]
    assert first.id == influencer["id"]
    assert first.audience_size == 0.364
    assert first.audience_makeup == 0.506
    assert first.posts_per_week == 0.425
    assert first.engagement_per_audience == 0.026
    assert first.tone_of_voice == 1.0
    assert first.relevant_events == 0.003
    assert first.relevant_works == 0.062
    assert first.rating == 0.341
