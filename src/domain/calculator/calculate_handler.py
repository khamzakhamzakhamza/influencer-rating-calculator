from typing import List
from .metric_normalizers.audience_size_normalizer import AudienceSizeNormalizer
from .metric_normalizers.audience_makeup_normalizer import AudienceMakeupNormalizer
from .calculate_request import CalculateRequest
from .calculate_response import CalculateResponse

class CalculateHandler:
	def calculate(self, request: CalculateRequest) -> List[CalculateResponse]:
		rating = []
		metrics = []

		for influencer in request.influencers:
			metrics.append(AudienceSizeNormalizer().normalize(influencer.audience))
			metrics.append(AudienceMakeupNormalizer().normalize(influencer.audience))
		
		rating.append(CalculateResponse(id=influencer.id, rating=0.75))
		return rating
