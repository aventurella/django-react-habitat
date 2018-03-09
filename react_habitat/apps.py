import logging
from django.apps import AppConfig
from .services import ReactHabitatRegistry

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "react_habitat"
    label = "react_habitat"
    verbose_name = "React Habitat"

    def ready(self):
        pass

    def get_registry(self, request):
        registry = None

        try:
            registry = request.__react_registry
        except AttributeError:
            registry = self.create_registry()
            request.__react_registry = registry

        return registry

    def create_registry(self):
        registry = ReactHabitatRegistry()
        return registry