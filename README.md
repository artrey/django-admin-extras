## Installation

For installing django-admin-extras, just run this command in your shell

```bash
pip install django-admin-extras
```

### Settings

```python
INSTALLED_APPS = (
    # ...
    'django_admin_extras',
    # ...
)
```

## Examples

Here is a simple Django model:

```python
from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    text = models.CharField(max_length=256)
    checked = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
```

Here is a simple Django admin for models above:

```python
from django.contrib import admin
from django.db.models import Q

from django_admin_extras import InputFilter, custom_titled_filter, custom_view_field

from .models import TodoItem


class TodoItemTextFilter(InputFilter):
    parameter_name = 'todoitem__text'
    title = 'todo item text'

    def queryset(self, request, queryset):
        if self.value() is not None:
            q = Q()
            for text_part in self.value().split():
                q &= Q(text__icontains=text_part)
            return queryset.filter(q)


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = 'text', 'custom_text', 'checked', 'custom_bool',
    list_filter = TodoItemTextFilter, ('checked', custom_titled_filter('test title for checked filter')),

    @custom_view_field(admin_order_field='-text')
    def custom_text(self, obj: TodoItem) -> str:
        return obj.text + ' custom'

    @custom_view_field(boolean=True, short_description='Not checked')
    def custom_bool(self, obj: TodoItem) -> bool:
        return not obj.checked
```
