# import bittensor
from fastapi import APIRouter

router = APIRouter()

# /api/python/bittensor/subnets
@router.get("/bittensor/subnets")
def read_bittensor():
    return {"message": "listing all subnets."}
