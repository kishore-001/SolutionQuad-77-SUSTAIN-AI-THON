from fastapi import APIRouter

router = APIRouter()


@router.get("/api")
def read_root():
    return {"message": "Welcome to the Innovation Center API"}