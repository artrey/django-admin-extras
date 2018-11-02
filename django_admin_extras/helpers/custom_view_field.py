from functools import wraps


def custom_view_field(*args, **kwargs):
    """
    Implements the wrapped admin view column with attributes from kwargs

    :param args: not used
    :param kwargs: attributes of column such as short_description, admin_order_field, boolean, etc.
    :return: decorated function
    """

    def decorated_func(func):
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            return func(*func_args, **func_kwargs)

        for k, v in kwargs.items():
            setattr(wrapper, k, v)
        return wrapper

    return decorated_func
