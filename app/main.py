from fastapi import FastAPI, Depends
from app.db import async_session
from sqlmodel.ext.asyncio.session import AsyncSession
from app.routes.films import router as films_router



app = FastAPI(title="Book Rental System")
        
app.include_router(films_router)

@app.get("/health")
async def health():
    return {"status": "ok"}
