from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateField('Created', auto_now_add=True)
    modified_at = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Is Active?', default=True)

    class Meta:
        abstract = True
