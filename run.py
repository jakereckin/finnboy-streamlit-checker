import os

from py.streamlit_checker import check_site
import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    try:
        logging.info(msg='Starting log')
        check_site.check_site(url=os.getenv('NDA_GBB_SITE'))
        check_site.check_site(url=os.getenv('GOLF_SITE'))
    except Exception as e:
        logging.exception(msg=f'An error occurred: {e}')
    finally:
        logging.info(msg='Finished processing')
    return None

if __name__ == '__main__':
    main()
