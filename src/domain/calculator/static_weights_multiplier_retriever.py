from typing import Dict
from .weights_multiplier_retriever_protocol import WeightsMultiplierRetriever

class StaticWeightsMultiplierRetriever:
    def get_weights(self) -> Dict[str, float]:
        return {
			"audience_size": 2,
			"audience_makeup": 2,
			"posts_per_week": 1,
			"engagement_per_audience": 3,
			"relevant_events": 1,
			"relevant_works": 2,
			"tone_of_voice": 3,
		}
