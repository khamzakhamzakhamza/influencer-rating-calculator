from pydantic import BaseModel

class CalculateResponse(BaseModel):
	id: str
	rating: float
