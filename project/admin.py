from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Project


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project


class ProjectAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ProjectResource
    list_display = ['title', 'created_at', 'category']
    search_fields = ['title'] 
    list_filter = ['title'] 

admin.site.register(Project, ProjectAdmin)
