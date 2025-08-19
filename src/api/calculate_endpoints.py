from typing import List
from fastapi import APIRouter
from ..domain.influencer import Influencer

router = APIRouter(
	prefix="/calculate",
	tags=["Calculate"]
)

@router.post("/")
def calculate_rating(influencers: List[Influencer]):
	return {"message": "Rating calculated successfully!"}