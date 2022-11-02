"""
Unit tests for http library

Contains unit tests for the http section of the package. It ensures that
HTTP responses are correctly profiled.

Typical Usage:
    $ pytest -v
"""

import pytest
from httpx import Cookies

from urlprofiler.http.request import Request

@pytest.fixture
def requests():
    """
    Fetches a URL and provides fixture for tests

    Instantiates the Request object and fetches the URL of an HTTP
    response service: HTTPBin.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    request = Request("https://httpbin.org/redirect/2")
    return request

def test_request_instantiation(requests): 
    """
    Tests the instantiation of the request object

    Ensures that the item generated by the Request class is in fact an
    object.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    assert isinstance(requests, object)

def test_status_code(requests):
    """
    Tests status code resolver

    Ensures that a status code is properly returned and translated into
    a string

    Args:
        requests fixture
    
    Returns:
        None
    
    Raises:
        None 
    """

    status_response = requests.get_status_code()

    status_code = status_response["http_status"]["status_code"]
    status_info = status_response["http_status"]["status_info"]

    assert isinstance(status_code, int) and isinstance(status_info, str)

def test_track_url(requests):
    """
    Test track URL history resolver

    Checks the track URL history resolver to ensure that redirect history
    is correctly captured and stored within a dictionary.

    Args:
        requests: pytest fixture
    
    Returns:
        None
    
    Raise:
        None
    """

    url_history = requests.track_url()
    expected_output = {
        "was_redirected": True,
        "redirect_history": None,
        "end_url": "https://httpbin.org/redirect/2"
    }
    assert url_history == expected_output

def test_get_connection_data(requests):
    """
    Tests get_connection_data method

    Ensures that connection data is accurately extracted from an HTTP 
    request. Checks to ensure a dictionary is returned.

    Args:
        requests - pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """ 

    connection_details = requests.get_connection_data()
    latency = connection_details["Latency (seconds)"]
    http_version = connection_details["HTTP Version"]
    cookies = hasattr(connection_details["Cookies"], "__class__")
    assert isinstance(latency, float) and isinstance(http_version, str) and cookies
