"""
Unit tests for profile_url.py

Tests the method within profile_url.py, to ensure it correctly extracts and
returns URL profiling data from a URL or hostname.

Typical Usage:
    $ pytest -v
"""

import sys

from urlprofiler.profile.profile_url import profile_url
from urlprofiler.profile.profile_url import profile_url_cli

def test_profile_url():
    """
    Connects to host and fetches metadata

    To test profile_url, a remote host is supplied and metadata extracted. This
    data is then examined, to ensure it has been returned as expected.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    fetched_metadata = profile_url("http://httpbin.org")

    assert isinstance(fetched_metadata, dict)

def test_profile_url_with_hostname():
    """
    Provides hostname to profile_url()

    By default, profile_url() expects to receive a URL. It can however
    append http:// to a given hostname, to fetch a response from that
    URL. This method tests this functionality.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    fetched_metadata = profile_url("httpbin.org")

    assert isinstance(fetched_metadata, dict)

def test_profile_url_with_argv(capsys):
    """
    Tests profile_url with sys.argv

    Mocks input from sys.argv and ensures that profile_url can correctly
    handle that input. It should return data within a dictionary.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    sys.argv = ["urlprofiler", "https://httpbin.org"]
    metadata = profile_url_cli()
    captured = capsys.readouterr()
    assert 'url' in captured.out

def test_profile_url_with_no_argv(capsys):
    """
    Tests profile_url with no sys.argv

    Mocks input from sys.argv, but doesn't supply a URL to the urlprofiler
    tool. A prompt should be printed to the console, providing guidance
    on typical usage.

    Args:
        capsys: standard output capture fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    sys.argv = ["urlprofiler"]
    metadata = profile_url_cli()
    captured = capsys.readouterr()
    assert 'Usage' in captured.out

def test_profile_url_with_multiple_args(capsys):
    """
    Tests profile_url with mulitple args

    Mocks input from sys.argv, providing multiple URLs to urlprofiler. The
    tool should iterate through the list and return data for each provided
    URL.

    Args:
        capsys: standard output capture fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    sys.argv = ["urlprofiler", "https://httpbin.com", "https://example.com"]
    metadata = profile_url_cli()
    captured = capsys.readouterr().out
    filtered_capture = filter(None, captured.split("\n"))
    assert len(list(filtered_capture)) == 54
