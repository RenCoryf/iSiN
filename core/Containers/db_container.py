from dependency_injector import containers, providers
from core.Services.DB_service.DB_configuration.db_config import DatabaseInit
from core.Services.DB_service.DB_configuration.db_session import Database
from ..config import config


class DBContainer(containers.DeclarativeContainer):

    configuration = providers.Singleton(DatabaseInit, config=config)

    db = providers.Singleton(Database, db=configuration)

    session_factory = providers.Callable(db.provided.session)
