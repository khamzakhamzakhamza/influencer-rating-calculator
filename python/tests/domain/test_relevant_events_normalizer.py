import pytest
from src.domain.calculator.metric_normalizers.relevant_events_normalizer import RelevantEventsNormalizer

@pytest.mark.parametrize("value, expected", [
    (0, 0.0),
    (10, 0.062),
    (20, 0.25),
    (40, 1.0),
    (45, 1.0)
])
def test_normalize_when_valid_values_should_normalize(value, expected):
    # Arrange
    normalizer = RelevantEventsNormalizer()

    # Act
    normalized_value = normalizer.normalize(value)

    # Assert
    assert normalized_value == expected
