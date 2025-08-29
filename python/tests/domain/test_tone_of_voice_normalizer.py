import pytest
from src.domain.calculator.metric_normalizers.tone_of_voice_normalizer import ToneOfVoiceNormalizer
from src.domain.tone_of_voice import ToneOfVoice

@pytest.mark.parametrize("value, expected", [
    ("scientific", 1.0),
    ("educational", 1.0),
    ("professional", 1.0),
    ("comedic", 0.5),
    ("motivational", 0.5),
    ("conversational", 0.5),
    ("provocative", 0.0)
])
def test_normalize_when_valid_values_should_normalize(value, expected):
    # Arrange
    normalizer = ToneOfVoiceNormalizer()

    # Act
    normalized_value = normalizer.normalize(ToneOfVoice(value))

    # Assert
    assert normalized_value == expected
