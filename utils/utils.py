import inspect
import logging
import time
from functools import wraps

logger = logging.getLogger('timing')


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        c = inspect.stack()[1][0].f_locals.get('self').__class__.__name__
        f = func.__name__
        logger.critical(f'TIMING ({c}.{f}): {int((end_time - start_time) * 1000)} ms')
        return res
    return wrapper


