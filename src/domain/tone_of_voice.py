from enum import Enum

class ToneOfVoice(str, Enum):
    SCIENTIFIC = "scientific "
    EDUCATIONAL = "educational"
    PROFESSIONAL = "professional"
    COMEDIC = "comedic"
    MOTIVATIONAL = "motivational"
    CONVERSATIONAL = "conversational"
    PROVOCATIVE = "provocative"
