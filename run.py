import os

from py.streamlit_checker import check_site
import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    checks = (
        ('NDA GBB site', lambda: check_site.check_site(url=os.getenv('NDA_GBB_SITE'))),
        ('NDA GBB database', lambda: check_site.check_database(
            connection=os.getenv('NDA_GBB_DB_CONNECTION'),
            database_name='NDA GBB',
        )),
        ('Golf site', lambda: check_site.check_site(url=os.getenv('GOLF_SITE'))),
        ('Golf database', lambda: check_site.check_database(
            connection=os.getenv('GOLF_DB_CONNECTION'),
            database_name='Golf',
        )),
    )
    failed_checks = []
    try:
        logging.info(msg='Starting log')
        for name, check in checks:
            try:
                check()
            except Exception:
                logging.exception('Check failed: %s', name)
                failed_checks.append(name)
    finally:
        logging.info(msg='Finished processing')

    if failed_checks:
        raise RuntimeError(f'Failed checks: {", ".join(failed_checks)}')

    return None

if __name__ == '__main__':
    main()
