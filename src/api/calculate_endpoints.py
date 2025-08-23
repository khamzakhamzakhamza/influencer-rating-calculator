from typing import List
from fastapi import APIRouter
from ..domain.calculator.calculate_handler import CalculateHandler
from ..domain.calculator.calculate_request import CalculateRequest
from ..domain.calculator.calculate_response import CalculateResponse

router = APIRouter(
	prefix="/calculate",
	tags=["Calculate"]
)

@router.post("/", response_model=List[CalculateResponse])
def calculate_rating(request: CalculateRequest):
	handler = CalculateHandler()
	return handler.calculate(request)	
