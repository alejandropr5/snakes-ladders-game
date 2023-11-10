import pytest

from snakesladders.game import SnakesAndLadders


@pytest.fixture(scope="session")
def snakesladders_obj():
    return SnakesAndLadders()
