from fastapi import APIRouter, Query, Body
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/nth-largest")
def nth_largest(n: int = Query(..., description="Which largest number to return"), 
                raw_body: str = Body(..., media_type="text/plain")):
    try:
        # Convert comma-separated values to integers
        nums = [int(x.strip()) for x in raw_body.split(',') if x.strip().isdigit()]
        
        if not nums:
            return JSONResponse(status_code=400, content={"error": "No valid numbers provided."})
        
        if n <= 0 or n > len(nums):
            return JSONResponse(status_code=400, content={"error": "Invalid value of n"})
        
        sorted_nums = sorted(nums, reverse=True)
        return {"nth_largest": sorted_nums[n - 1]}
    
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
