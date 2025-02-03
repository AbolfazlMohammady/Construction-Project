import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'  
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'  
    context_object_name = 'project'


def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Project.objects.filter(title__icontains=query)
    return render(request, 'project/products_search.html', {'results': results, 'query': query})


def project_chart_view(request):
    projects = Project.objects.all().order_by('created_at')

    project_names = [project.title for project in projects]
    project_years = [project.created_at.year for project in projects if project.created_at]

    chart_data = json.dumps({
        'labels': project_names,
        'data': project_years
    })

    return render(request, 'project/project_chart.html', {'chart_data': chart_data})
