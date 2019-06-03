from django.contrib import admin
from.models import Resepi

# Register your models here.


class ResepiAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredients', 'process', 'image', 'created_by']


admin.site.register(Resepi, ResepiAdmin)
