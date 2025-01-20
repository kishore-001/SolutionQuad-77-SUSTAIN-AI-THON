from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import api , random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins temporarily 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers

app.include_router(api.router)
app.include_router(random.router)