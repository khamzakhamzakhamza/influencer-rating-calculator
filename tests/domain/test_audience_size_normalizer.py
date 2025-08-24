import pytest
from src.domain.audience import Audience
from src.domain.calculator.metric_normalizers.audience_size_normalizer import AudienceSizeNormalizer

@pytest.mark.parametrize("value, expected", [
    (0, 0.025),
    (2500, 0.574),
    (5000, 0.758),
    (1_000_000, 1.0),
    (1_000_001, 1.0),
])
def test_normalize_when_valid_values_should_normalize(value, expected):
    # Arrange
    normalizer = AudienceSizeNormalizer()

    # Act
    normalized_value = normalizer.normalize(
        Audience(size=value, executive=0, professionals=0)
    )

    # Assert
    assert normalized_value == expected
