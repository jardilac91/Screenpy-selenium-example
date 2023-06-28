from typing import Generator

from screenpy import Actor
from screenpy.pacing import the_narrator

from screenpy_selenium.abilities import BrowseTheWeb

from screenpy_adapter_allure import AllureAdapter

import pytest


@pytest.fixture(scope="function", name="Usuario")
def fixture_actor() -> Generator:
    """Inicializamos el usuario y le entregamos la habilidad navegar en internet utilizando chrome"""
    actor = Actor.named("Usuario").who_can(BrowseTheWeb.using_chrome())
    yield actor
    actor.exit()

"""Agregamos el adaptador de allure para generar los reportes"""
the_narrator.adapters.append(AllureAdapter())

URL = "https://google.com"