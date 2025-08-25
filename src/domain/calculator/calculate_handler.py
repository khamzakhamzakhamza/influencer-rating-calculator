from typing import List
from .rating_calculator import RatigCalculator
from .metric_normalizers.tone_of_voice_normalizer import ToneOfVoiceNormalizer
from .metric_normalizers.relevant_events_normalizer import RelevantEventsNormalizer
from .metric_normalizers.relevant_works_normalizer import RelevantWorksNormalizer
from .metric_normalizers.engagement_per_audience_normalizer import EngagementPerAudienceNormalizer
from .metric_normalizers.posts_per_week_normalizer import PostsPerWeekNormalizer
from .metric_normalizers.audience_size_normalizer import AudienceSizeNormalizer
from .metric_normalizers.audience_makeup_normalizer import AudienceMakeupNormalizer
from .calculate_request import CalculateRequest
from .calculate_response import CalculateResponse

class CalculateHandler:
	def calculate(self, request: CalculateRequest) -> List[CalculateResponse]:
		rating: List[CalculateResponse] = []

		for influencer in request.influencers:
			metrics = {
				'audience_size': AudienceSizeNormalizer().normalize(influencer.audience),
				'audience_makeup': AudienceMakeupNormalizer().normalize(influencer.audience),
				'posts_per_week': PostsPerWeekNormalizer().normalize(influencer.audience, influencer.posts),
				'engagement_per_audience': EngagementPerAudienceNormalizer().normalize(influencer.audience, influencer.posts),
				'relevant_events': RelevantEventsNormalizer().normalize(influencer.relevant_events_count) if request.topic else 0.0,
				'relevant_works': RelevantWorksNormalizer().normalize(influencer.relevant_works_count) if request.topic else 0.0,
				'tone_of_voice': ToneOfVoiceNormalizer().normalize(influencer.tone_of_voice)
			}

			rating.append(CalculateResponse(id=influencer.id, rating=RatigCalculator().calculate(metrics), **metrics))

		return rating
