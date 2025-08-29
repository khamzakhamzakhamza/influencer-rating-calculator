from typing import List, Optional
from pydantic import BaseModel
from ..influencer import Influencer

class CalculateRequest(BaseModel):
	topic: Optional[str] = None
	influencers: List[Influencer]
