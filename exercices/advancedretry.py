from functools import wraps
import random
import time

class MaxRetriesExceededError(Exception):
    def __init__(self, total_attempts, last_exception):
        self.total_attempts = total_attempts
        self.last_exception = last_exception
        msg = f"Failed after {self.total_attempts} tries with error : {self.last_exception}."
        super().__init__(msg)

def retry_with_backoff(max_attempts, base_delay=1.0, jitter=0.1):
    """
    A decorator factory for retrying a function with validation, exponential
    backoff, jitter, and custom exceptions.
    """
    if not isinstance(max_attempts, int) or max_attempts <= 0:
        raise ValueError("Max attempts should be an interger greater than zero.")
    if not isinstance(base_delay, int) or base_delay <= 0:
        raise ValueError("Base delay should be an interger greater than zero.")
    if not isinstance(jitter, int) or jitter <= 0:
        raise ValueError("Jitter should be an interger greater than zero.")
    
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):          
            failure_count = 0
            while failure_count <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if failure_count <= max_attempts:
                        failure_count += 1
                        delay = base_delay * (2 ** (failure_count -1))
                        delay += random.uniform(0, jitter)
                        time.sleep(delay)
                        continue
                    else:
                        raise MaxRetriesExceededError(total_attempts=failure_count, last_exception=e)                
        return wrapper
    return decorator
