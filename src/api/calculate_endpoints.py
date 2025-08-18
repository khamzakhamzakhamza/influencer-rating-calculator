from fastapi import APIRouter

router = APIRouter(
	prefix="/calculate",
	tags=["Calculate"]
)

@router.get("/")
def calculate_rating():
	return {"message": "Rating calculated successfully!"}