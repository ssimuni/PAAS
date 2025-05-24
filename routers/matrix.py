from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/multiply")
def multiply_matrices(raw_input: str = Body(..., media_type="text/plain")):
    try:
        parts = raw_input.strip().split('\n\n')  # Split by empty line

        if len(parts) != 2:
            return JSONResponse(status_code=400, content={"error": "Input must have two matrices separated by a blank line."})

        # Parse both matrices
        def parse_matrix(block):
            return [list(map(int, row.split())) for row in block.strip().split('\n')]

        m1 = parse_matrix(parts[0])
        m2 = parse_matrix(parts[1])

        # Validate matrix sizes
        if len(m1[0]) != len(m2):
            return JSONResponse(status_code=400, content={"error": "Matrix multiplication not possible. Columns of m1 must equal rows of m2."})

        # Multiply matrices
        result = [
            [sum(a * b for a, b in zip(row, col)) for col in zip(*m2)]
            for row in m1
        ]

        return {"result": result}

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
