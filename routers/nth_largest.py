from fastapi import APIRouter

router = APIRouter()

@router.post("/nth-largest")
def nth_largest(nums: list[int], n: int):
    sorted_nums = sorted(nums, reverse=True)
    return {"nth_largest": sorted_nums[n - 1]}