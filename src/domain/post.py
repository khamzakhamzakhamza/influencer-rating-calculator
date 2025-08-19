from datetime import datetime
from pydantic import BaseModel

class Post(BaseModel):
	id: str
	time: datetime
	text: str
	views: int
	reactions: int
	comments: int
