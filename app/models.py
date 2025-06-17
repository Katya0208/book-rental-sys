# app/models.py

from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String, Numeric, SmallInteger, TIMESTAMP, Boolean, Integer

class Film(SQLModel, table=True):
    # По умолчанию SQLModel возьмет имя таблицы "film"
    film_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(String(length=255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(String))  # text в схеме
    release_year: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    language_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    original_language_id: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    rental_duration: int = Field(sa_column=Column(SmallInteger), nullable=False)
    rental_rate: float = Field(sa_column=Column(Numeric(precision=4, scale=2)), nullable=False)
    length: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    replacement_cost: float = Field(sa_column=Column(Numeric(precision=5, scale=2)), nullable=False)
    rating: Optional[str] = Field(default=None, sa_column=Column(String(length=10)))  
    # В Pagila rating — enum/text; здесь mapping на str
    special_features: Optional[List[str]] = Field(
        default=None,
        sa_column=Column(ARRAY(String), nullable=True)
    )
    last_update: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)), nullable=False)


class Actor(SQLModel, table=True):
    actor_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column(String(length=45)), nullable=False)
    last_name: str = Field(sa_column=Column(String(length=45)), nullable=False)
    last_update: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)), nullable=False)


class Customer(SQLModel, table=True):
    customer_id: Optional[int] = Field(default=None, primary_key=True)
    store_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    first_name: str = Field(sa_column=Column(String(length=45)), nullable=False)
    last_name: str = Field(sa_column=Column(String(length=45)), nullable=False)
    email: Optional[str] = Field(default=None, sa_column=Column(String(length=50)))  # может быть NULL
    address_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    activebool: bool = Field(sa_column=Column(Boolean), nullable=False)
    create_date: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)), nullable=False)
    last_update: Optional[datetime] = Field(default=None, sa_column=Column(TIMESTAMP(timezone=False)))
    # В Pagila есть поле active (int)? Обычно activebool достаточен. Если есть active int:
    # active: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))


class Rental(SQLModel, table=True):
    rental_id: Optional[int] = Field(default=None, primary_key=True)
    rental_date: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)), nullable=False)
    inventory_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    customer_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    return_date: Optional[datetime] = Field(default=None, sa_column=Column(TIMESTAMP(timezone=False)))
    staff_id: int = Field(sa_column=Column(SmallInteger), nullable=False)
    last_update: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)), nullable=False)