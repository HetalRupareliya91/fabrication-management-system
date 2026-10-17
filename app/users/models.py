"""SQLAlchemy model for Users."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<User id={self.id}>"
