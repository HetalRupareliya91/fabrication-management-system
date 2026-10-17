"""Application settings loaded from environment variables."""
import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Settings:
    app_name: str = field(default_factory=lambda: os.getenv("APP_NAME", "Fabrication Management System"))
    database_url: str = field(default_factory=lambda: os.getenv("DATABASE_URL", "sqlite:///./fabrication.db"))


settings = Settings()
