"""Docstring for shared_library."""

import pytest

from shared_library.singleton import SingletonMeta


@pytest.fixture
def model():
    """Class Fixture."""

    class Test(metaclass=SingletonMeta):
        pass

    return Test


def test_model(model):
    """Test class does not have multiple instances."""
    assert model() == model()
