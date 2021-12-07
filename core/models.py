from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateField('Created', auto_now_add=True)
    modified_at = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Is Active?', default=True)

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Stock')
    image = StdImageField('Image', upload_to='products', variations={'thumb': {'width': 480, 'height': 480}})
    slug = models.SlugField('Slug', max_length=150, blank=True, editable=False)

    def __str__(self):
        return self.name
