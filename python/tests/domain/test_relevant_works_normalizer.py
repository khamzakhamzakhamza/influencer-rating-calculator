import pytest
from src.domain.calculator.metric_normalizers.relevant_works_normalizer import RelevantWorksNormalizer

@pytest.mark.parametrize("value, expected", [
    (0, 0.0),
    (10, 0.25),
    (15, 0.562),
    (20, 1.0),
    (25, 1.0)
])
def test_normalize_when_valid_values_should_normalize(value, expected):
    # Arrange
    normalizer = RelevantWorksNormalizer()

    # Act
    normalized_value = normalizer.normalize(value)

    # Assert
    assert normalized_value == expected
