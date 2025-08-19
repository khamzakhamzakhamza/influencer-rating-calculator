from typing import List
from fastapi import APIRouter
from .calculate_request import CalculateRequest
from .calculate_response import CalculateResponse

router = APIRouter(
	prefix="/calculate",
	tags=["Calculate"]
)

@router.post("/", response_model=List[CalculateResponse])
def calculate_rating(request: CalculateRequest):
	response = [CalculateResponse(id = 'example_id', rating = 0.75)]
	return response