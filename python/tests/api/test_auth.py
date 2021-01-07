# -*- coding: utf-8 -*-
import pytest

from client import TodoAppApiException


@pytest.mark.api
def test_api_authentication_success_token(api):
    # sign in with the default user's credentials (using token mode).
    token = api.authenticate("QA", "willWin")
    assert token.username == "QA"


@pytest.mark.api
@pytest.mark.parametrize(
    "username,password", [("abc", "def"), ("", "willWin"), ("QA", "")]
)
def test_api_authentication_failed_token(api, username, password):
    # sign in with bad credentials using token mode (shall fail).
    with pytest.raises(TodoAppApiException) as e_info:
        api.authenticate(username, password)
    assert "HTTP 401" in str(e_info.value)
