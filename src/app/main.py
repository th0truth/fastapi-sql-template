from starlette.middleware.cors import CORSMiddleware
# from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse 

from prometheus_fastapi_instrumentator import Instrumentator

from core.config import settings

app = FastAPI(
  title=settings.NAME,
  description=settings.DESCRIPTION,
  summary=settings.SUMMARY,
  version=settings.VERSION,
  openapi_url="/api/openapi.json",
  # lifespan=lifespan
)


@app.get("/health",
  tags=["Health Check"],
  summary="Perform a Health Check",
  response_description="Return HTTP Status Code 200 (OK)",
  status_code=status.HTTP_200_OK)
async def healt_check():
  return JSONResponse(
    content={"status": "Ok"}
  )

# Set all CORS enabled origins
if settings.all_cors_origins:
  # Add middlewares
  app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
  )

# Instrument the app (adds metrics like request count, latency, etc.)
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

# Include main router to the app
# app.include_router(api_main_router)