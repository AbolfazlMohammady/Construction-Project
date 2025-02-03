from django.urls import path
from .views import ProjectListView, ProjectDetailView, search, project_chart_view

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('search/', search, name='search'),
    path('chart/', project_chart_view, name='project_chart')
]
