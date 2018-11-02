from abc import ABC
from django.contrib import admin


def custom_titled_filter(title: str):
    class Wrapper(admin.FieldListFilter, ABC):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper
