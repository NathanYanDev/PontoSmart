from config import Base

from typing import List

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    position: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    attendances: Mapped[List['Attendance']] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r}, email={self.email!r}, position={self.position!r})'
    