"""
Some features extends django.contrib.admin
"""

from .helpers import custom_titled_filter, custom_view_field
from .filters import InputFilter

__version__ = '1.0.2'

__all__ = '__version__', 'custom_titled_filter', 'custom_view_field', 'InputFilter',
