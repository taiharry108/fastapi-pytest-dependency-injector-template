import pytest
import asyncio

from dependency_injector import providers

from container import Container
from core.database_service import DatabaseService

@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    c = Container()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope="module")
async def database():
    container = Container()
    container.db.override(providers.Singleton(
        DatabaseService, db_url="postgresql+asyncpg://USERNAME:PASSWORD@SERVER:PORT/DB_NAME"))
    db = container.db()
    await db.create_database()
    return db
