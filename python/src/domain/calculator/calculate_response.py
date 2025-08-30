from typing import Optional
from pydantic import BaseModel

class CalculateResponse(BaseModel):
	id: str
	name: str
	audience_size: float
	audience_makeup: float
	posts_per_week: float
	engagement_per_audience: float
	relevant_events: Optional[float] = None
	relevant_works: Optional[float] = None
	tone_of_voice: float
	rating: float
