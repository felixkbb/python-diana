from .injector import Injector, NoProvider  # noqa
from .module import Module, provider, contextprovider, provides  # noqa

__version__ = "3.1.0"

injector = Injector()
