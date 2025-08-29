from typing import Protocol, Dict

class WeightsMultiplierRetriever(Protocol):
    def get_weights(self) -> Dict[str, float]:
        ...
