import asyncio
from datetime import date

from config import dict_fuel_urls
from models.fuel import FuelType, FuelPrice
from scrapers.globalpetrolprices import scrape_fuel


async def get_prices(fuel_type: FuelType) -> list[FuelPrice]:
    list_models = []
    today = date.today()
    raw = await scrape_fuel(dict_fuel_urls[fuel_type])

    for item in raw:
        country, price = list(item.items())[0]
        list_models.append(FuelPrice(
            country=country,
            fuel_type=fuel_type,
            price_usd=float(price),
            date=today
        ))

    return list_models


