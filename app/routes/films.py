from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from app.db import async_session
from app.models import Film
from sqlmodel.ext.asyncio.session import AsyncSession
from app.main import get_session

router = APIRouter(prefix="/films", tags=["films"])

@router.get("/")
async def read_films(q: str = Query(None), session: AsyncSession = Depends(get_session)):
    stmt = select(Film)
    if q:
        stmt = stmt.where(Film.title.ilike(f"%{q}%"))
    result = await session.exec(stmt)
    films = result.all()
    return films