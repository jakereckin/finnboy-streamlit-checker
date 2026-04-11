import logging
import time
import os
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

# ============================================================================
def get_logger() -> None:
    parent_path = Path(__file__).parent.parent.parent
    LOG_FILE_NAME = os.path.join(parent_path, 'log/process_log.log')
    file_handler = TimedRotatingFileHandler(
        filename=LOG_FILE_NAME,
        when='midnight',
        interval=1,
        backupCount=10
    )
    logging.basicConfig(
        handlers=[file_handler], 
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %H:%M'
    )
    return None

# ============================================================================
def timer(func):
    def wrapper(*arg, **kw):
        start = time.perf_counter()
        res = func(*arg, **kw)
        end = time.perf_counter()
        my_time = round(end-start, 2)
        LOG.info(f'{func.__name__}: {my_time}')
        return res
    return wrapper


# ============================================================================
def start_log() -> None:
    LOG.info('__RUN START__')
    return None


# ============================================================================
def end_log() -> None:
    LOG.info('__RUN END__\n')
    return None


# ============================================================================
def log_exception(exception) -> None:
    LOG.info(msg=exception, exc_info=True)
    return None

LOG = logging.getLogger(name=__name__)