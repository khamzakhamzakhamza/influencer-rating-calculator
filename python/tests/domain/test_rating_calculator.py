import pytest
from src.domain.calculator.rating_calculator import RatigCalculator

@pytest.mark.parametrize("metrics, expected", [
    (
        {
            "audience_size": 0.5,
            "audience_makeup": 0.7,
            "posts_per_week": 0.6,
            "engagement_per_audience": 0.4,
            "tone_of_voice": 1.0
        },
        0.64
    ),
    ({"m": 1.0}, 1.0),
    ({"a": 1.0, "b": 1.0, "c": 0.0}, 0.667),
    ({"a": 1.0, "b": 1.0}, 1.0),
])
def test_calculate_when_given_valid_metrics_should_calculate_rating(metrics, expected):
    # Arrange
    calc = RatigCalculator()

    # Act
    rating = calc.calculate(metrics)

    # Assert
    assert rating == expected
