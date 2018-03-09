from typing import Set, Any, Dict
from django.template.loader import render_to_string


class ReactHabitatRegistry():
    def __init__(self):
        self.reset()

    def register(self, component_name: str, **kwargs: Dict[str, Any]):
        self.collection.add(component_name)
        return self.create_component(component_name, **kwargs)

    def create_component(self, component_name: str, **kwargs: Dict[str, Any]):
        return ReactHabitatComponent(component_name, **kwargs)

    def bootstrap(self):
        return ReactHabitatBootstrap(self)

    def reset(self):
        self.collection: Set[str] = set()

class ReactHabitatComponent:
    def __init__(self, component_name, **props):
        self.component_name = component_name
        self.props = props


    def render(self) -> str:
        context = {
            'component_name': self.component_name,
            'props': self.props
        }

        return render_to_string('react-habitat-component.html', context)

    def __str__(self):
        return self.render()


class ReactHabitatBootstrap:
    def __init__(self, registry: ReactHabitatRegistry):
        self.registry = registry

    def render(self) -> str:

        if not self.registry.collection:
            return ""

        context = {
            'components': self.registry.collection,
        }

        return render_to_string('react-habitat-bootstrap.js', context)

    def __str__(self):
        return self.render()
