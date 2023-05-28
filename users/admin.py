from django.contrib import admin
from .models import Profiles, Skill


@admin.register(Profiles)
class profilesAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class skillAdmin(admin.ModelAdmin):
    pass
# Register your models here.
