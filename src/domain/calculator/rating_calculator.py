from src.domain.di_setup import get_weights_retriever
from .weights_multiplier_retriever_protocol import WeightsMultiplierRetriever

class RatigCalculator:
	def __init__(self, retriever: WeightsMultiplierRetriever | None = None):
		self._retriever = retriever or get_weights_retriever()

	def calculate(self, metrics: dict) -> float:
		weights = {}

		for metric in metrics:
			# TODO: Make configurable weights
			weights[metric] = 1.0 / len(metrics)

		rating = 0.0
		for metric in metrics:
			rating += metrics[metric] * weights[metric]

		return round(rating, 3)
