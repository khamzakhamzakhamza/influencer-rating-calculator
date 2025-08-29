from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
	id: str
	time: datetime
	text: str
	views: Optional[int] = None
	reactions: int
	comments: int
	reposts: int
