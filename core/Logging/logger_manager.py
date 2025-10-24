import logging
from logging import Logger
from logging.handlers import RotatingFileHandler


class LoggerManager:

    def __init__(
        self,
        log_file: str = "logs/core.log",
        max_bytes: int = 50_000_000,
        backup_count: int = 1,
    ):
        self.log_file = log_file
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.loggers: dict[str, Logger] = {}

    def get_logger(self, name: str, level: int = logging.INFO) -> Logger:
        if name in self.loggers:
            return self.loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Файл с ротацией
        file_handler = RotatingFileHandler(
            self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.propagate = False

        self.loggers[name] = logger
        return logger
