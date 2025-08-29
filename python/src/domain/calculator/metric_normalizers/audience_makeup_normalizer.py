from ...audience import Audience

class AudienceMakeupNormalizer:
	def normalize(self, audience: Audience) -> float:
		if audience.size == 0:
			return 0
		
		if audience.executive + audience.professionals > audience.size:
			raise ValueError("Invalid audience makeup: sum of executives and professionals exceeds total size")
		
		w_exec = 1
		w_prof = 0.5

		exec_frac = audience.executive / audience.size
		prof_frac = audience.professionals / audience.size

		score  = (w_exec * exec_frac) + (w_prof * prof_frac)
		return round(min(1.0, score), 3)
