from src.domain.tone_of_voice import ToneOfVoice

class ToneOfVoiceNormalizer:
	def normalize(self, tone_of_voice: ToneOfVoice) -> float:
		match tone_of_voice:
			case ToneOfVoice.SCIENTIFIC | ToneOfVoice.EDUCATIONAL | ToneOfVoice.PROFESSIONAL:
				return 1.0
			case ToneOfVoice.COMEDIC | ToneOfVoice.MOTIVATIONAL | ToneOfVoice.CONVERSATIONAL:
				return 0.5
			case ToneOfVoice.PROVOCATIVE:
				return 0
