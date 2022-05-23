import logging


def count_calls(func):
    def decorator(*args, **kwargs):
        logging.log(1, msg=f"{func.__name__} calls: {decorator.calls}")
        decorator.calls += 1
        return func(*args, **kwargs)

    decorator.calls = 0
    return decorator





