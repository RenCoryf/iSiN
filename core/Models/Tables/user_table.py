# models/user.py
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from .base_table import BaseTable


class User(BaseTable):
    __tablename__ = "users"

    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(255), nullable=True)

    tasks = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete-orphan",
    )
