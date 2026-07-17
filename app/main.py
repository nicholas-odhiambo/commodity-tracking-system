from fastapi import FastAPI
from app.apis.routes.commodity import router as commodity_router
from app.apis.routes.supplier import router as supplier_router
from app.apis.routes.warehouse import router as warehouse_router
from app.apis.routes.customer import router as customer_router


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the commodity tracking system."}

app.include_router(commodity_router)
app.include_router(supplier_router)
app.include_router(warehouse_router)
app.include_router(customer_router)