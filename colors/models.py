from django.db.models import Model
from django.db.models.fields import CharField

class ColorModel(Model):
    name = CharField(max_length=100)
    bg_css_class = CharField(max_length=100)
    text_css_class = CharField(max_length=100)

    class Meta:
        abstract = True