from config import Base

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime, timezone

from models.enums import AttendanceTypeEnum

class Attendance(Base):
    __tablename__ = 'attendance'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    date_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    type: Mapped['AttendanceTypeEnum'] = mapped_column(SQLEnum(AttendanceTypeEnum, name="attendance_type_enum"),nullable=False)
    latitude: Mapped[str] = mapped_column(String(10), nullable=False)
    longitude: Mapped[str] = mapped_column(String(10), nullable=False)
    proximity_place: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    user: Mapped['User'] = relationship(back_populates='attendances')

    def __repr__(self) -> str:
        return f'id={self.id!r}, user_id={self.user_id!r}, date_time={self.date_time!r}, type={self.type!r}, lat={self.latitude!r}, long={self.longitude!r}, proximity_place={self.proximity_place}'