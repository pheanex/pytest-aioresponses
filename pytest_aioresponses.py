import aioresponses as aioresponses_
import pytest


@pytest.fixture
def aioresponses():
    with aioresponses_.aioresponses() as aior:
        yield aior
