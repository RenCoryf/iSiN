from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from contextlib import asynccontextmanager
from .db_config import DatabaseInit


class Database:
    def __init__(self, db: DatabaseInit):
        self.url = db.url
        self.engine = db.engine
        self.async_sessionmaker = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def session(self):
        async with self.async_sessionmaker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            else:
                await session.commit()
