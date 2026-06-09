from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.fuel import FuelType
from services.fuel_service import get_prices
router = APIRouter(prefix="/prices", tags=["prices"])

@router.get("/{fuel_type}")
async def get_fuel_prices(fuel_type: FuelType):
    return await get_prices(fuel_type)
