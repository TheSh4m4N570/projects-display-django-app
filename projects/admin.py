from django.contrib import admin
from .models import Project, Tag, Review

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

