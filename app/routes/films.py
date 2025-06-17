# app/routes/films.py
from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models import Film
from app.deps import get_session

router = APIRouter(prefix="/films", tags=["films"])


@router.get("/")
async def read_films(
    q: str | None = Query(None),
    session: AsyncSession = Depends(get_session),
):
    stmt = select(Film)
    if q:
        stmt = stmt.where(Film.title.ilike(f"%{q}%"))

    result = await session.execute(stmt)          # ← используем execute
    films = result.scalars().all()                #  .scalars() → объекты Film
    return films
