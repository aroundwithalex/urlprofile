"""
Tests URL and hostname validation

Tests both URL and hostname validation, to ensure that correctly formatted
URLs and hostnames are successfully returned whereas invalid ones raise an
Exception.

Typical Usage:
    $ pytest -v
"""

import pytest

from urlprofiler.url.validator import validate_url
from urlprofiler.url.validator import validate_hostname
from urlprofiler.url.validator import UrlException
from urlprofiler.url.validator import HostnameException


def test_validate_url_with_valid_url():
    """
    Tests validate_url with valid URL

    Provides a valid URL to validate_url, and ensures that the function
    returns the URL as expected.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    url = "https://www.example.com"

    valid_url = validate_url(url)

    assert valid_url == url

def test_validate_url_fails_with_no_scheme():
    """
    Tests validate_url fails with no scheme

    Ensures the validate_url method fails when the supplied URL lacks a
    scheme such as http or https.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_url = "www.example.com"

    with pytest.raises(UrlException):
        validate_url(invalid_url)
    
def test_validate_url_fails_with_no_domain():
    """
    Tests validate_url fails with no domain

    Ensures the validate_url method fails when no domain is supplied. A
    TLD is passed to the method instead.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_url = ".com"

    with pytest.raises(UrlException):
        validate_url(invalid_url)
    
def test_validate_url_fails_with_no_suffix():
    """
    Tests validate_url fails with no suffix

    Ensures the validate_url method fails when no suffix is supplied. It
    should raise a UrlException error.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_url = "invalid_domain"
    
    with pytest.raises(UrlException):
        validate_url(invalid_url)
    
def test_validate_hostname_with_valid_host():
    """
    Tests validate_hostname with valid host

    Ensures validate_hostname function successfully returns a hostname
    if it is considered valid.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    host_name = "google.com"

    valid_host_name = validate_hostname(host_name)

    assert valid_host_name == host_name

def test_validate_hostname_with_no_domain():
    """
    Tests validate_hostname with invalid domain

    Ensures that validate_hostname raises an exception if a hostname
    is supplied that lacks a domain.  A HostnameException should be
    raised instead.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    with pytest.raises(HostnameException):
        validate_hostname(".com")

def test_validate_hostname_with_no_suffix():
    """
    Tests validate_hostname with no suffix

    Ensures validate_hostname raises an exception if the supplied hostname
    lacks a suffix. A HostnameException should be raised instead.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    with pytest.raises(HostnameException):
        validate_hostname("google")

def test_hostname_formatting():
    """
    Tests hostnames formating in validate_hostname

    Part of the validate_hostname method returns a formatted hostname, which
    contains the subdomain, domain and suffix of the supplied hostname. This
    is designed to help deal with situations where whole URLs are supplied.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    
    url = "https://another.example.com"
    expected_output = "another.example.com"

    formatted_hostname = validate_hostname(url)

    assert formatted_hostname == expected_output
