from django.urls import path
from .views import ProjectListView, ProjectDetailView, search, project_chart_view , project_management, delete_project

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('search/', search, name='search'),
    path('chart/', project_chart_view, name='project_chart'),
    path('management/', project_management, name='project-management'),
    path('management/delete/<int:project_id>/', delete_project, name='delete-project'),
]