# app/models.py

from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String, Numeric, SmallInteger, TIMESTAMP, Boolean, Integer

class Film(SQLModel, table=True):
    film_id: Optional[int] = Field(default=None, primary_key=True)

    title: str = Field(sa_column=Column(String(255)))

    description: Optional[str] = Field(
        default=None,
        sa_column=Column(String)          # text по умолчанию nullable
    )

    release_year: Optional[int] = Field(
        default=None,
        sa_column=Column(SmallInteger)
    )

    language_id: int = Field(
        sa_column=Column(SmallInteger)  # ← nullability только здесь
    )

    original_language_id: Optional[int] = Field(
        default=None,
        sa_column=Column(SmallInteger)
    )

    rental_duration: int = Field(
        sa_column=Column(SmallInteger)
    )

    rental_rate: float = Field(
    sa_column=Column(Numeric(4, 2, asdecimal=False))
    )

    length: Optional[int] = Field(
        default=None,
        sa_column=Column(SmallInteger)
    )

    replacement_cost: float = Field(
    sa_column=Column(Numeric(5, 2, asdecimal=False))
    )

    rating: Optional[str] = Field(
        default=None,
        sa_column=Column(String(10))
    )

    special_features: Optional[List[str]] = Field(
        default=None,
        sa_column=Column(ARRAY(String))
    )

    last_update: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=False))
    )


class Actor(SQLModel, table=True):
    actor_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column(String(length=45)))
    last_name: str = Field(sa_column=Column(String(length=45)))
    last_update: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)))


class Customer(SQLModel, table=True):
    customer_id: Optional[int] = Field(default=None, primary_key=True)
    store_id: int = Field(sa_column=Column(SmallInteger))
    first_name: str = Field(sa_column=Column(String(length=45)))
    last_name: str = Field(sa_column=Column(String(length=45)))
    email: Optional[str] = Field(default=None, sa_column=Column(String(length=50)))  # может быть NULL
    address_id: int = Field(sa_column=Column(SmallInteger))
    activebool: bool = Field(sa_column=Column(Boolean))
    create_date: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)))
    last_update: Optional[datetime] = Field(default=None, sa_column=Column(TIMESTAMP(timezone=False)))
    # В Pagila есть поле active (int)? Обычно activebool достаточен. Если есть active int:
    # active: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))


class Rental(SQLModel, table=True):
    rental_id: Optional[int] = Field(default=None, primary_key=True)
    rental_date: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)))
    inventory_id: int = Field(sa_column=Column(SmallInteger))
    customer_id: int = Field(sa_column=Column(SmallInteger))
    return_date: Optional[datetime] = Field(default=None, sa_column=Column(TIMESTAMP(timezone=False)))
    staff_id: int = Field(sa_column=Column(SmallInteger))
    last_update: datetime = Field(sa_column=Column(TIMESTAMP(timezone=False)))