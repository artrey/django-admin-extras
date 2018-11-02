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
