from sqlalchemy.ext.asyncio import create_async_engine
from core.Models.Tables.base_table import Base
from core.config import Config


class DatabaseInit:
    def __init__(self, config: Config):
        self.url = self._db_url(
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            db_name=config.POSTGRES_DB,
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
        )
        self.engine = create_async_engine(self.url, echo=True, future=True)

    async def init_db(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def _db_url(
        self, user: str, password: str, db_name: str, host: str, port: str
    ) -> str:
        return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
