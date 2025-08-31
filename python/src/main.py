import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .api.calculate_endpoints import router as calculate_router

app = FastAPI()

frontend_dir = os.path.join(os.path.dirname(__file__), "../../node/dist")
app.mount("/static", StaticFiles(directory=frontend_dir, html=True), name="static")

origins = [
    "http://localhost:5173",   # React dev server
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",   
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
    index_path = os.path.join(frontend_dir, "index.html")
    return FileResponse(index_path)

@app.get("/assets/{file}")
async def read_asset(file: str):
    asset_path = os.path.join(frontend_dir, "assets", file)
    return FileResponse(asset_path)

@app.exception_handler(ValueError)
async def value_error_handler(_: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
