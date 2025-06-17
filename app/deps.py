# app/deps.py
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends

from app.db import async_session

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
