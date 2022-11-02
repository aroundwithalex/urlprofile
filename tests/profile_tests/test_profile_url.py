"""
Unit tests for profile_url.py

Tests the method within profile_url.py, to ensure it correctly extracts and
returns URL profiling data from a URL or hostname.

Typical Usage:
    $ pytest -v
"""

from urlprofiler.profile.profile_url import profile_url

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
