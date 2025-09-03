from datetime import datetime, timezone
import math
import statistics
from typing import List
from ...audience import Audience
from ...post import Post

class PostsPerWeekNormalizer:
	def normalize(self, audience: Audience, posts: List[Post],  now: datetime = datetime.now(timezone.utc)) -> float:
		max_days = 84  # 12 weeks
		weeks_to_posts = [0] * 12

		for post in [p for p in posts if (now - p.time).days <= max_days]:
			delta_days = (now - post.time).days
			week_number = max(1, math.ceil(delta_days / 7)) - 1
			weeks_to_posts[week_number] += 1

		avg_posts = statistics.mean(weeks_to_posts)
		expected_avg = self._expected_avg(audience)
		dropoff = self._expected_dropoff(audience)
		
		return round(max(0, 1 - abs(avg_posts - expected_avg) / dropoff), 3)
	
	def _expected_avg(self, audience: Audience) -> float:
		if audience.size < 5000:
			return 2.3
		if audience.size < 10000:
			return 2.8
		if audience.size < 25000:
			return 5.0
		if audience.size < 100_000:
			return 5.1
		return 7.5
	
	def _expected_dropoff(self, audience: Audience) -> float:
		if audience.size < 5000:
			return 2.5
		if audience.size < 10000:
			return 3
		if audience.size < 25000:
			return 5.5
		if audience.size < 100_000:
			return 5.5
		return 6
