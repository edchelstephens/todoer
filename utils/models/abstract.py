from django.db import models

class DatetimeCreatedModel(models.Model):
    """Abstrace base class to watch datetime creations for statistics."""

    datetime_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True