class RelevantWorksNormalizer:
	def normalize(self, relevant_works: int) -> float:
		return round(min(1, pow(relevant_works / 20, 2)), 3)
