from threading import local
from django import template
from django.apps import apps
from ..services import ReactHabitatRegistry


register = template.Library()
_thread_locals = local()


@register.simple_tag
def react_habitat_component(component_name, **kwargs):
    registry: ReactHabitatRegistry = apps \
        .get_app_config('react_habitat') \
        .get_registry(_thread_locals)

    component = registry.register(component_name, **kwargs)
    return component.render()


@register.simple_tag
def react_habitat_bootstrap():
    registry: ReactHabitatRegistry = apps \
        .get_app_config('react_habitat') \
        .get_registry(_thread_locals)

    bootstrap = registry.bootstrap()
    result = bootstrap.render()

    registry.reset()
    return result
