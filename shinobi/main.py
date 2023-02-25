from fastapi import FastAPI

import routers.authentication

app = FastAPI()

app.include_router(routers.authentication.router)


@app.get("/")
def hello_world():
    return {"Hello": "asd"}
