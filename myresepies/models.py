# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Resepi(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.TextField()
    process = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True, )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=30, default='user')

    def __str__(self):
        return self.name
