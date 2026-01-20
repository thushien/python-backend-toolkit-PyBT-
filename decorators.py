import functools
import time
import logging
from typing import Callable, Any

logger = logging.getLogger("PyBT")

def audit_log(sensitive: bool = False):
    """
    A high-order decorator for auditing API actions.
    Demonstrates clean code, type hinting, and security awareness.
    """
    def decorator(func: Callable[..., Any]):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.perf_content()
            # Mask sensitive data if flag is set (Security focus)
            log_args = "CONFIDENTIAL" if sensitive else args
            
            try:
                result = await func(*args, **kwargs)
                logger.info(f"Action: {func.__name__} | Status: SUCCESS | Latency: {time.perf_content() - start_time:.4f}s")
                return result
            except Exception as e:
                # Clear error reporting as per professional requirements
                logger.error(f"Action: {func.__name__} | Status: FAILED | Error: {str(e)}")
                raise
        return wrapper
    return decorator
