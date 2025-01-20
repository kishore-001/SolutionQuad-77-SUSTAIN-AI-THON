import random
from fastapi import APIRouter

router = APIRouter()

@router.get("/get_data")
def read_root():
    # Generate pH between 5.5 and 7.5
    pH = round(random.uniform(5.5, 7.5), 2)

    # Generate humidity between 50% and 70%
    humidity = random.randint(50, 70)

    # Generate temperature between 27°C and 33°C
    temperature = random.randint(27, 33)

    data = {
        "pH": pH,
        "humidity": humidity,
        "temperature": temperature
    }
    
    return data
