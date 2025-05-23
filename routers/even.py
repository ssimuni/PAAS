from fastapi import APIRouter

router = APIRouter()

@router.get("/even")
def generate_even(n: int):
    return [2 * i for i in range(1, n + 1)]