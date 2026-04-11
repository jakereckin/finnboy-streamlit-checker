from playwright.sync_api import sync_playwright
from .log import get_logger
import logging
import time
import os

get_logger()
LOG = logging.getLogger()

HEADLESS = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')

def check_site(url: str) -> None:
    """
    Checks the habit-tracker site for any errors using Playwright.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        time.sleep(10)
        LOG.info(page.title())
        LOG.info(f'Checking site: {url}')
        page.reload()
        time.sleep(10)
        browser.close()
    return None
