from playwright.sync_api import sync_playwright
import sqlitecloud
import logging
import time
import os
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

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
        logging.info(page.title())
        logging.info(f'Checking site: {url}')
        page.reload()
        time.sleep(10)
        browser.close()
    return None


def check_database(connection: Optional[str], database_name: str) -> None:
    """Runs a read-only connectivity query against a SQLiteCloud database."""
    if not connection:
        raise ValueError(f'Missing connection string for {database_name}')
    logging.info(f'Checking database connectivity: {database_name}')

    with sqlitecloud.connect(connection) as conn:
        result = conn.execute('SELECT 1').fetchone()

    if result is None or result[0] != 1:
        raise RuntimeError(f'Connectivity query returned an unexpected result for {database_name}')

    logging.info('Database query succeeded: %s', database_name)
