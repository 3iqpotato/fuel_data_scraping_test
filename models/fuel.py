from datetime import date
from pydantic import BaseModel
from enum import Enum

class FuelType(str, Enum):
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    LPG = "lpg"

class FuelPrice(BaseModel):
    country: str
    fuel_type: FuelType
    price_usd: float
    date: date

class CountryPrices(BaseModel):
    country: str
    date: str
    prices: dict[FuelType, float | None]