from fastapi import FastAPI
from fastapi.responses import JSONResponse
from time import sleep

from .Containers.db_container import DBContainer
from .Containers.logger_container import LoggerContainer
from .Models.Tables.user_table import User


app = FastAPI(title="Core Service")
logger_manager = LoggerContainer.logger_manager()


async def main():
    logger = logger_manager.get_logger("main")
    logger.info("Waiting for db to start...")
    sleep(2)
    db = DBContainer.db()
    logger.info(f"-------------{db.url}-------------")
    # async with db.session() as session:
    #     new_user = User(telegram_id=1234567890, name="John Doe")
    #     session.add(new_user)
    #     result = await session.execute("SELECT * FROM users")
    #     users = result.fetchall()
    #     logger.info(f"Users: {users}")


@app.on_event("startup")
async def on_startup():
    await main()


@app.get("/health", summary="Health check", tags=["System"])
async def health_check():
    return JSONResponse(
        status_code=200, content={"status": "ok", "message": "Service is healthy"}
    )
