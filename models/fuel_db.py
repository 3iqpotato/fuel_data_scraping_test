from sqlalchemy import Column, Integer, String, Float, Date, UniqueConstraint
from database import Base
from datetime import date

class FuelPrice(Base):
    __tablename__ = "fuel_prices"

    id          = Column(Integer, primary_key=True)
    country     = Column(String, nullable=False)
    fuel_type   = Column(String, nullable=False)
    price_eur   = Column(Float, nullable=False)
    recorded_at = Column(Date, nullable=False, default=date.today)

    __table_args__ = (
        UniqueConstraint("country", "fuel_type", "recorded_at"),
        # не записва дубликати за същия ден
    )