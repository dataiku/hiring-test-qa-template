# -*- coding: utf-8 -
import requests

from .token import Token


class TodoAppApiException(Exception):
    """Default Exception for the REST API client"""

    def __init__(self, message, status_code, content):
        """An exception occurs in the REST API client.

        Arguments:
            message {str} -- the reason of the exception
            status_code {int} -- HTTP status code
            content {type} -- the response body
        """
        self.message = message
        self.status_code = status_code
        self.content = content

    def __repr__(self):
        return f"{self.message}: (HTTP {self.status_code}) - {self.content}"

    def __str__(self):
        return f"{self.message}: (HTTP {self.status_code}) - {self.content}"


def check_status(response, expected_status, error_message):
    if not response.status_code == expected_status:
        raise TodoAppApiException(error_message, response.status_code, response.text)


class ClientAPI(object):
    """REST API client for the QA dataiku TodoApp."""

    def __init__(self, base_url):
        """Init

        Arguments:
            base_url {str} -- the base URL of the API
        """
        self.base_url = base_url
        self.session = requests.Session()

    def authenticate(self, username, password):
        """User authentication

        Arguments:
            username {str} -- the username
            password {str} -- the password

        Raises:
            TodoAppApiException: unable to get the token

        Returns:
            str -- the token (or None if the authorization method is basic)
        """
        payload = {"username": username, "password": password}
        response = self.session.post(f"{self.base_url}/authenticate", json=payload)

        check_status(response, 200, "Authentication failed")

        token = Token().from_json(response.json())

        self.session.auth = (token.token, "dataiku")

        return token

    def reset(self):
        """Reset the database

        Raises:
            TodoAppApiException: unable to reset the database
        """
        response = self.session.get(f"{self.base_url}/reset")

        check_status(response, 200, "Unable to reset app")
