from dependency_injector import containers, providers
from core.some_service import SomeService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["tests.test_some_service"])
    config = providers.Configuration(yaml_files=["config.yml"])


    some_service_factory = providers.FactoryAggregate(
        s=providers.Singleton(
            SomeService
        ),
    )

    some_service = providers.Singleton(
        some_service_factory, config.some_service.name)
