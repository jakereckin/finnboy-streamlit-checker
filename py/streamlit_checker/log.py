import logging
import time
import os



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