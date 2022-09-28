from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy import orm

from core.some_service import SomeService
from core.database_service import DatabaseService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["routers.main"])
    config = providers.Configuration(yaml_files=["config.yml"])

    some_service_factory = providers.FactoryAggregate(
        s=providers.Singleton(
            SomeService
        ),
    )

    some_service = providers.Singleton(
        some_service_factory, config.some_service.name)

    db_engine = providers.Singleton(
        create_async_engine, config.db.url, echo=False)

    db_session_maker = providers.Singleton(
        orm.sessionmaker,
        autocommit=False,
        autoflush=False,
        bind=db_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    db_service = providers.Singleton(
        DatabaseService, db_engine, db_session_maker)
