"""Docstring for shared_library."""

from typing import Any
import pytest

from shared_library.pydantic_exts import BaseModelSingleton, BaseSettingsSingleton


@pytest.fixture
def model():
    """Model Fixutre."""

    class TestModel(BaseModelSingleton):
        def model_post_init(self, context: Any) -> None:
            super().model_post_init(context)

    return TestModel


def test_model(model):
    """Test Singleton Model."""
    assert model() == model()


@pytest.fixture
def settings():
    """Settings Fixture."""

    class TestSettings(BaseSettingsSingleton):
        def model_post_init(self, context: Any) -> None:
            super().model_post_init(context)

    return TestSettings


def test_settings(settings):
    """Test Singleton Settings."""
    assert settings() == settings()
