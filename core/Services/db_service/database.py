from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from contextlib import asynccontextmanager
from core.Services.db_service.db_config import Database_init


class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_async_engine(
            self.db_url,
            echo=True,
            future=True
        )
        self.async_sessionmaker = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    @asynccontextmanager
    async def get_session(self):
        async with self.async_sessionmaker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            else:
                await session.commit()
