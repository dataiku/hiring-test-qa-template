# -*- coding: utf-8 -
import pytest

from client import ClientAPI


@pytest.fixture(scope="session", autouse=True)
def reset(base_url):
    ClientAPI(base_url).reset()


@pytest.fixture
def api(base_url):
    return ClientAPI(base_url)
