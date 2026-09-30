import requests
from datetime import datetime, timezone


DEFAULT_TIMEOUT = 30

DEFAULT_HEADER = {
    "User-Agent": "LIFZ-Corpus/0.1 (+https://github.com/ronnakrit221/LIFZ-Corpus)"
}


def fetch_url(url: str) -> dict:
    """
    Fetch raw content from a URL.

    INPUT:
        url: str

    RETURN:
        dict containing raw data and metadata
    """

    try:
        response = requests.get(
            url,
            headers=DEFAULT_HEADER,
            timeout=DEFAULT_TIMEOUT,
            allow_redirects=True,
        )

        return {
            "success": True,
            "url": url,
            "final_url": response.url,
            "status_code": response.status_code,
            "content_type": response.headers.get("Content-Type"),
            "headers": dict(response.headers),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "encoding": response.encoding,
            "html": response.text,
            "error": None,
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "url": url,
            "error": "Request timed out",
        }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "url": url,
            "error": "Connection error",
        }

    except requests.exceptions.InvalidURL:
        return {
            "success": False,
            "url": url,
            "error": "Invalid URL",
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "url": url,
            "error": str(error),
        }