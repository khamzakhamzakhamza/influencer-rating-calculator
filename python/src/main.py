from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .api.calculate_endpoints import router as calculate_router

app = FastAPI()

origins = [
    "http://localhost:5173",   # React dev server
    "http://localhost:8080",
    "http://127.0.0.1:8080",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculate_router)

@app.get("/")
async def read_root():
    return Response(status_code=200)

@app.exception_handler(ValueError)
async def value_error_handler(_: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
