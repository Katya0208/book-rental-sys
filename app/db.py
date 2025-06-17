from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_async_engine(settings.database_url, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    # при использовании существующей БД Pagila: не вызывать SQLModel.metadata.create_all,
    # т.к. схема уже есть. Этот метод оставляем для своих таблиц, но для Pagila опираемся на существующие.
    pass
