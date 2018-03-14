# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cat, Owner, Breeder, Litter


# Register your models here.
admin.site.register(Cat),
admin.site.register(Owner),
admin.site.register(Breeder),
admin.site.register(Litter)