from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DatabaseInit:
    def __init__(
        self, user: str, password: str, db_name: str, host: int = 5432, port: int = 5432):
        self.db_url = self._get_db_url(user, password, db_name, host, port)
        self.engine = create_async_engine(self.db_url, echo=True, future=True)

    async def init_db(self)->None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def _get_db_url(
        self, user: str, password: str, db_name: str, host: int, port: int) -> str:
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
