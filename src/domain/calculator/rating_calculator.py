class RatigCalculator:
	def calculate(self, metrics: dict) -> float:
		weights = {}

		for metric in metrics:
			# TODO: Make configurable weights
			weights[metric] = 1.0 / len(metrics)

		rating = 0.0
		for metric in metrics:
			rating += metrics[metric] * weights[metric]

		return round(rating, 3)
