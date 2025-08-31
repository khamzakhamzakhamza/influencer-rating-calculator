from ...audience import Audience

class AudienceSizeNormalizer:
	def normalize(self, audience: Audience) -> float:
		return round(min(1, pow((1 + audience.size) / 100_000, 0.4)), 3)
