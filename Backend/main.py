from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import api, random, predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(api.router)
app.include_router(random.router)
app.include_router(predict.router)
