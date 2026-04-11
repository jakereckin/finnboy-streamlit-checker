from config.service import get_config
from py.streamlit_checker import check_site, log


def main() -> None:
    try:
        log.start_log()
        CONFIG = get_config()
        check_site.check_site(url=CONFIG.get('NDA_GBB_SITE'))
        check_site.check_site(url=CONFIG.get('GOLF_SITE'))
    except Exception as e:
        log.log_exception(exception=e)
    finally:
        log.end_log()
    return None

if __name__ == '__main__':
    main()
