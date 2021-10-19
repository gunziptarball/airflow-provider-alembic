import pathlib

import pytest


@pytest.fixture
def project_root():
    """Root of the project"""
    return pathlib.Path(__file__).parent.parent
