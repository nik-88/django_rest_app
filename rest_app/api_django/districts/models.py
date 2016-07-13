from __future__ import unicode_literals
import datetime
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class District(models.Model):
    Name = models.CharField(max_length=50, blank=False, default='')
    Campuses = models.CharField(max_length=150, blank=True)
    DateCreated = models.DateTimeField(default=datetime.datetime.utcnow())

    class Meta:
        ordering = ('Name',)


class Campus(models.Model):
    Name = models.CharField(max_length=50, blank=False, default='')
    DistrictId = models.ForeignKey(District, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(default=datetime.datetime.utcnow())

    class Meta:
        ordering = ('Name',)
