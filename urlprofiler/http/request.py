"""
Makes a HTTP request and returns the response

Utilises the HTTPX library to make a HTTP request and returns the response
and associated data, such as whether the URL redirected.

Typical Usage:
    >>> from urlprofiler.http.request import Request
    >>> Request.get_status_code()
    200
"""

import httpx
from http.client import responses 

class Request:

    """ 
    Makes a HTTP request and returns resulting data

    This class contains various methods that fetch a URL, return the status
    code and indicate whether the URL redirected. It also returns the actual
    URL that was resolved by the HTTP request.

    Attributes:
        self.session: HTTP session generated by HTTPX
    """

    def __init__(self, url, timeout=60):
        """
        Constructor for the Requests object

        Takes a URL and uses HTTPX to fetch various attributes, which can then
        be queried for status codes, redirects and more.

        Args:
            url: URL to be profiled
        
        Returns:
            None
        
        Raises:
            None
        """

        self.url = url
        self.response = httpx.get(url, timeout=timeout)
    
    def get_status_code(self):
        """
        Returns the status code and its meaning

        Queries the response object for the status code of a URL and fetches
        its meaning from the httplib library. Returns both as a dictionary.

        Args:
            None
        
        Returns:
            Status code and meaning as dictionary e.g.,
            {200: "OK"}
        
        Raises:
            None
        """

        status_code = self.response.status_code
        meaning = responses[status_code]

        return {status_code: meaning}
    
    def track_url(self):
        """
        Checks for redirects and returns actual URL

        Looks through the response history to check for redirects and returns 
        the actual URL that was resolved.

        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
        """

        metadata = {
            "was_redirected": False,
            "redirect_history": None,
            "url": self.url
        }

        if self.response.is_redirect:
            metadata["was_redirected"] = True
        
        if self.response.history:
            metadata["redirect_history"] = self.response.history
        
        if self.response.url != self.url:
            metadata["url"] = self.response.url
        
        return metadata

    def get_connection_data(self):
        """
        Fetches data points about HTTP connection

        Gets various data points about the HTTP connection, including the
        http version used, the time elapsed in the request and associated
        cookies.

        Args:
            None
        
        Returns:
            Dictionary with latency, HTTP Version and cookies e.g.,
            {
                "Latency: 1s,
                "HTTP Version": "HTTP/2",
                "Cookes": ["Yum Yum"]
            }
        
        Raises: 
            None
        """

        latency = self.response.elapsed.total_seconds()
        http_version = self.response.http_version
        cookies = self.response.cookies

        return {
            "Latency (seconds)": latency,
            "HTTP Version": http_version,
            "Cookies": cookies
        }