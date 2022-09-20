from fastapi import APIRouter, Depends

from container import Container
from dependency_injector.wiring import inject, Provider, Provide
from dependency_injector import providers

from core.some_service import SomeService

router = APIRouter()


@router.get("/test")
@inject
async def hello_world(
            some_service: SomeService = Depends(
                Provide[Container.store_service]
            ),
            some_service_factory: providers.FactoryAggregate = Depends(
                Provider[Container.some_service_factory]
            ),
        ):        
    print(some_service)
    print(some_service_factory)
    

    return {"hello": "world!"}

