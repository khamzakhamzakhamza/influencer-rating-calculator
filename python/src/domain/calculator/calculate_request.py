from typing import List
from pydantic import BaseModel
from ..influencer import Influencer

class CalculateRequest(BaseModel):
	influencers: List[Influencer]
