from fastapi import FastAPI, Response
from .api.calculate_endpoints import router as calculate_router

app = FastAPI()

app.include_router(calculate_router)

@app.get("/")
def read_root():
    return Response(status_code=200)
