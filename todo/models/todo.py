from django.db import models
from django.conf import settings

from utils.models.abstract import DatetimeCreatedModel

class Todo(DatetimeCreatedModel):
    """Our todo model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todos"
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    is_completed = models.BooleanField(default=False)
    datetime_completed = models.DateTimeField(blank=True, null=True)
   
    class Meta:
        app_label = "todo"
        db_table = "todos"

    def __repr__(self) -> str:
        return "Todo(pk={}, title={}, user={})".format(
            self.pk,
            self.title,
            self.user
        )

    def __str__(self) -> str:
        return self.title
