from fastapi import FastAPI
from routers import prices_api

app = FastAPI(
    title="Fuel Prices API",
    description="Цени на горива в Европа",
    version="1.0.0"
)

app.include_router(prices_api.router)

@app.get("/")
async def root():
    return {"message": "API работи — виж /docs"}

