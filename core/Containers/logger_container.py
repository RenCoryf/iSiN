from dependency_injector import containers, providers
from ..Logging.logger_manager import LoggerManager


class LoggerContainer(containers.DeclarativeContainer):
    logger_manager = providers.Singleton(LoggerManager)
