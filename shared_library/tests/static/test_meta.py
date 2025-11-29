"""Docstring for shared_library."""

import pytest

from shared_library.static import StaticMeta


@pytest.fixture
def model():
    """Class Fixture."""

    class Test(metaclass=StaticMeta):
        pass

    return Test


def test_model(model):
    """Test class cannot be created."""
    with pytest.RaisesExc(NotImplementedError) as exc:
        model()
        assert exc
