from http.client import responses
from multiprocessing.managers import Value

from fastapi import FastAPI, Response, status
import requests
from utility import *

app = FastAPI()


@app.get("/api/classify-number", status_code=status.HTTP_200_OK)
def read_root(response : Response, number:int =0):
    number = number
    try:
        number= int(number)
    except ValueError:
        response.status_code =status.HTTP_400_BAD_REQUEST
        return {
    "number": "alphabet",
    "error": True
}
    url=f"http://numbersapi.com/{number}/math"

    fun_fact = requests.get(url).text
    data = {
    "number": number,
    "is_prime":is_prime(number),
    "is_perfect":is_perfect(number),
    "properties":find_property(number),
    "digit_sum":digit_sum(number),
    "fun_fact":fun_fact
}

    return data


