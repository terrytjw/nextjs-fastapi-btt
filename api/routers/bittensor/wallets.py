# import bittensor
from fastapi import APIRouter

router = APIRouter()

# /api/python/bittensor/wallets
@router.get("/bittensor/wallets") 
def gen_wallet():
    # wallet = bittensor.wallet()
    # wallet.create_new_coldkey()
    # wallet.create_new_hotkey()

    # print(f"Succesfully generated wallet. Here's the info:\n{wallet}")

    return {"message": "wallet created."}
