from typing import List
from pydantic import BaseModel
from .audience import Audience
from .tone_of_voice import ToneOfVoice
from .post import Post

class Influencer(BaseModel):
    id: str
    audience: Audience
    relevant_works_count: int
    relevant_events_count: int
    tone_of_voice: ToneOfVoice
    posts: List[Post]
    