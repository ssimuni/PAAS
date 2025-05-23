from fastapi import APIRouter

router = APIRouter()

@router.post("/multiply")
def multiply_matrices(m1: list[list[int]], m2: list[list[int]]):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*m2)] for row in m1]
    return {"result": result}