import pytest
from src.domain.audience import Audience
from src.domain.calculator.metric_normalizers.audience_makeup_normalizer import AudienceMakeupNormalizer

@pytest.mark.parametrize("value, exec, prof, expected", [
    (0, 0, 0, 0),
    (2500, 500, 1000, 0.4),
    (5000, 5000, 0, 1)
])
def test_normalize_when_valid_values_should_normalize(value, exec, prof, expected):
    # Arrange
    normalizer = AudienceMakeupNormalizer()
    audience = Audience(size=value, executive=exec, professionals=prof)

    # Act
    normalized_value = normalizer.normalize(audience)

    # Assert
    assert normalized_value == expected

def test_normalize_when_exec_plus_prof_exceeds_size_should_throw():
    # Arrange
    normalizer = AudienceMakeupNormalizer()
    audience = Audience(size=100, executive=60, professionals=50)

    # Act / Assert
    with pytest.raises(ValueError, match="Invalid audience makeup"):
        normalizer.normalize(audience)