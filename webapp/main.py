"""Application module."""

from logging import config

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from container import Container
from routers import main



config.fileConfig('logging.conf', disable_existing_loggers=False)


def create_app() -> FastAPI:
    container = Container()

    db = container.db_service()
    db.create_database()

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    setattr(app, 'container', container)

    app.include_router(main.router, prefix="/api")

    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "hello world!"}
