from typing import Optional
from pydantic import BaseModel

class CalculateResponse(BaseModel):
	id: str
	audience_size: float
	audience_makeup: float
	posts_per_week: float
	engagement_per_audience: float
	relevant_events: Optional[float]
	relevant_works: Optional[float]
	tone_of_voice: float
	rating: float
