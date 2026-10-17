"""FastAPI application factory. Every app/<module>/router.py is registered automatically."""
import importlib
import pkgutil
from contextlib import asynccontextmanager

from fastapi import FastAPI

import app as app_pkg
from app.core.config import settings
from app.core.database import Base, engine

SKIP_PACKAGES = {"core"}


def discover_routers():
    routers = []
    for info in sorted(pkgutil.iter_modules(app_pkg.__path__), key=lambda i: i.name):
        if not info.ispkg or info.name in SKIP_PACKAGES:
            continue
        module_name = f"app.{info.name}.router"
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError as exc:
            if exc.name == module_name:
                continue
            raise
        routers.append(module.router)
    return routers


@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


def create_app() -> FastAPI:
    application = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)
    for router in discover_routers():
        application.include_router(router, prefix="/api/v1")

    @application.get("/health", tags=["System"])
    def health():
        return {"status": "ok"}

    return application


app = create_app()
