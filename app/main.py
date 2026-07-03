from fastapi import FastAPI
from app.apis.routes.commodity import router as commodity_router


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the commodity tracking system."}

app.include_router(commodity_router)