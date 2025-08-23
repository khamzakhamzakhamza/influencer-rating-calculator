from typing import List
from ...audience import Audience
from ...post import Post

class AudienceSizeNormalizer:
	def normalize(self, audience: Audience, posts: List[Post]) -> float:

		# median_posts_per_week = posts
		return 0.5 # round(min(1, pow((1 + audience.size) / 10000, 0.4)), 3)
