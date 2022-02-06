import imp
from operator import imod
from django.contrib import admin
from .models import *

# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "description"]
    list_filter = ["name"]
    sreach_fields = ["name"]


class RateAdmin(admin.ModelAdmin):
    list_display = ["id", "meal", "user", "stars"]
    list_filter = ["meal", "user"]


admin.site.register(Meal, MealAdmin)
admin.site.register(Rate, RateAdmin)
