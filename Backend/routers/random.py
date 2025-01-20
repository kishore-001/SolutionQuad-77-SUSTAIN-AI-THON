from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/get_data")
def read_root():
    data = {
        "pH": random.uniform(5.5, 7.5),
        "moisture": random.randint(30, 80),
        "temperature": random.randint(20, 35)
    }
    return data
