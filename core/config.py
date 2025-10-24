from os import getenv


class Config:
    def __init__(self) -> None:
        self.POSTGRES_USER: str = str(getenv("POSTGRES_USER"))
        self.POSTGRES_PASSWORD: str = str(getenv("POSTGRES_PASSWORD"))
        self.POSTGRES_HOST: str = str(getenv("POSTGRES_HOST"))
        self.POSTGRES_PORT: str = str(getenv("POSTGRES_PORT"))
        self.POSTGRES_DB: str = str(getenv("POSTGRES_DB"))


config = Config()
