class RelevantEventsNormalizer:
	def normalize(self, relevant_events: int) -> float:
		return round(min(1, pow(relevant_events / 40, 2)), 3)
