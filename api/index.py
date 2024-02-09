# serves as a backend API that can be consumed by the Next.js frontend
# it defines routes, request handlers, and possibly the integration with databases or external services
from fastapi import FastAPI
import bittensor

from .routers.users import router as user_router
from .routers.items import router as item_router
from .routers.bittensor.subnets import router as subnets_router
from .routers.bittensor.wallets import router as wallets_router

app = FastAPI()


@app.get("/api/python")
def hello_world():
    subtensor = bittensor.subtensor()
    # subnets = subtensor.get_subnets()
    # print(f"Here's are all the:\n{subnets}")

    subnet_18_info = subtensor.get_subnet_info(18)
    subnet_18_owner_ss58 = subnet_18_info.owner_ss58
    subnet_18_burn = subnet_18_info.burn
    # print(f"Here's the owner's address for subnet 18:\n{subnet_18_owner_ss58}")

    return {"subnet_18_owner_address": subnet_18_owner_ss58, "subnet_18_burned": subnet_18_burn}

routers = [user_router, item_router, subnets_router, wallets_router]  # add more routers to this list as needed

for router in routers:
    app.include_router(router, prefix="/api/python")
# in package.json, the command `pip3 install -r requirements.txt && python3 -m uvicorn api.index:app --reload` does the following:
# - installs the python dependencies listed in requirements.txt
# - runs the FastAPI app with uvicorn (a ASGI server) with the app defined in api.index
# - --reload flag enables hot reloading, meaning that the server will auto-restart upon code changes