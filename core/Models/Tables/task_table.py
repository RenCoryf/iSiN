# models/task.py
from sqlalchemy import Column, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .base_table import BaseTable


class Task(BaseTable):
    __tablename__ = "tasks"

    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    deadline = Column(TIMESTAMP(timezone=True), nullable=True)

    user_id = Column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    user = relationship("User", back_populates="tasks")
