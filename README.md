# urlprofiler

**urlprofiler** fetches metadata about websites. For instance:

```
>>> from urlprofiler.profile.profile_url import profile_url
>>> metadata = profile_url("https://example.com")
>>> print(metadata)
{"url": "https://example.com", "was_redirected": True....}
```
urlprofiler makes it easy to access metadata about a URL, such as:

- HTTP status codes
- Connection latency
- SSL certificate information
- IP address of the hosting server

It can be imported as a Python package, or run directly on the command line using
`urlprofiler <URL>`. It can even take multiple URLs, and returns metadata in the order
the URLs are passed.

# Installing urlprofiler

urlprofiler is available on PyPI:

`$ python -m pip install urlprofiler`

Officially urlprofiler runs on 3.7 and above. It was built on a macOS operating system and 
has been tested on Linux. Don't forget to activate a virtual environment if you plan to use
`urlprofiler` within your own package:

`$ python -m venv venv`

# Data points & best practices

- HTTP status with string translation e.g., 200, OK
- Redirection history for the given URL
- Connection latency (in seconds)
- Cookies returned by the HTTP connection
- SSL certificate data, including: -
    - Issuer
    - Expiry Date
    - DNS names
    - Organization details
- IP address of host server

To achieve reliable results, be sure to supply a full URL, includng protocol, domain name 
and TLD. Please be aware that, if only a domain and TLD is supplied, `urlprofiler` will add 
`http` to the beginning of the supplied string.

# Cloning the repository and running the tests

You can clone the repository by using `git clone` followed by a link to this repository.

To run the tests, install pytest via `$ pip install pytest` in a virtual environment. 
You can then run the tests with `pytest -v`. Alternatively, you can install tox with 
`pip install tox` and run all associated tools (for code coverage, linting et al.) via `$ tox`. 

