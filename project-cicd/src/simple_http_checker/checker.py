import logging
import requests
from typing import Collection

logger = logging.getLogger(__name__)

def check_urls(urls: Collection[str], timeout: int = 5) -> dict[str, str]:
    """Check lists of URL and returns their status 

    Args:
        urls : List of URLs to check
        timeout : Maximum time in seconds to wait for each reaquest. Defaults to 5.

    Returns:
        A dictionary mapping each URL to its status
    """

    logger.info(f"Starting check for {len(urls)} URLs with timeout of {timeout}")
    results : dict[str, str] = {}

    for url in urls:
        status = "UNKNOWN"

        try:
            logger.debug(f"Checking : {url}.")
            response = requests.get(url, timeout=timeout)

            if response.ok:
                status = f"{response.status_code} OK"
            else:
                status = f"{response.status_code} {response.reason}"
        except requests.exceptions.Timeout:
            status = "TIMEOUT"
            logger.warning(f"Faced timeout to check {url}.")
        except requests.exceptions.ConnectionError:
            status = "CONNECTION_ERROR"
            logger.warning(f"Connection error for {url}.")
        except requests.exceptions.RequestException as e:
            status = f"REQUEST_ERROR: {type(e).__name__}"
            logger.error(f"Unexpected error for {url} : {e}")
        
        results[url] = status
        logger.debug(f"Checked : {url:<40} --> {status}") # better aligment
    
    logger.info("URL check finished.")
    return results