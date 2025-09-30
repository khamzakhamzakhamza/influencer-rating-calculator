from datetime import datetime, timezone
import statistics
from typing import List
from ...audience import Audience
from ...post import Post

class EngagementPerAudienceNormalizer:
	def normalize(self, audience: Audience, posts: List[Post],  now: datetime = datetime.now(timezone.utc)) -> float:
		if posts is None or len(posts) == 0:
			return 0.0
		
		if audience.executive + audience.professionals > audience.size:
			raise ValueError("Invalid audience makeup: sum of executives and professionals exceeds total size")
		
		max_days = 84  # 12 weeks
		engagement_to_posts = []

		for post in [p for p in posts if (now - p.time).days <= max_days]:
			engagement = post.reactions + post.comments + post.reposts
			engagement_to_posts.append(engagement / (audience.size + 1))

		median_engagement = statistics.median(engagement_to_posts)
		expected_median = self._expected_median(audience)
		
		return round(min(1, median_engagement / (expected_median * 2)), 3)
	
	def _expected_median(self, audience: Audience) -> float:
		if audience.size < 5000:
			return 0.24
		if audience.size < 10000:
			return 0.33
		if audience.size < 25000:
			return 0.11
		if audience.size < 100_000:
			return 0.09
		return 0.04
