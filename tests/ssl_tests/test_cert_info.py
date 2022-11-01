"""
Unit tests for SSL library

Contains various unit tests that ensure SSL information is correctly
retrieved from a hostname.  Also tests to ensure IP server data is also
correctly collected.

Typical Usage:
    $ pytest -v
"""

import pytest
from unittest.mock import patch
import ssl

from urlprofiler.ssl.cert_info import CertInfo

@pytest.fixture
def cert_info():
    """
    Instantiates CertInfo object for testing

    Constructs the CertInfo object, so that it can be used in testing
    various methods. These include fetching SSL certificate information
    and IP address data.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    cert_info = CertInfo("httpbin.org")
    return cert_info

def test_get_ssl_info(cert_info):
    """
    Tests retrieval of SSL certificate information

    Connects to a URL and ensures that SSL certificate data is correctly
    pulled from that hostname. It ensures that a dictionary is returned.

    Args:
        cert_info: pytest fixture containing CertInfo object
    
    Returns:
        None
    
    Raises:
        None
    """

    ssl_info = cert_info.get_ssl_info()
    assert isinstance(ssl_info, dict)

def test_get_ip_address_success(cert_info):
    """
    Tests retrieval of IP address of server

    Connects to a URL or hostname via a socket and fetches the IP address
    of the remote server. In this instance, the method should successfully
    return an IP address.

    Args:
        cert_info: pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    ip_address = cert_info.get_ip_address()
    assert isinstance(ip_address, dict)

def test_get_ip_address_fail(cert_info):
    """
    Tests get_ip_address fails with bad hostname

    Ensures that get_ip_address fails when a bad hostname is supplied. It should
    raise a socket error, which should generate a warning.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    with patch("socket.gethostbyname", side_effect=Exception()):
        with pytest.warns(UserWarning):
            cert_info.get_ip_address()
