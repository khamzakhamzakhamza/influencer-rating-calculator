from .calculator.static_weights_multiplier_retriever import StaticWeightsMultiplierRetriever
from .calculator.weights_multiplier_retriever_protocol import WeightsMultiplierRetriever

def get_weights_retriever() -> WeightsMultiplierRetriever:
    return StaticWeightsMultiplierRetriever()
