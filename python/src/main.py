from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from .api.calculate_endpoints import router as calculate_router

app = FastAPI()

app.include_router(calculate_router)

@app.get("/")
async def read_root():
    return Response(status_code=200)

@app.exception_handler(ValueError)
async def value_error_handler(_: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
