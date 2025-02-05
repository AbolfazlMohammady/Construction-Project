import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import ProjectForm


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



def is_superadmin(user):
    return user.is_superuser

@user_passes_test(is_superadmin)
def project_management(request):
    projects = Project.objects.all()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ پروژه با موفقیت اضافه شد!")
            return redirect('project-management')
    else:
        form = ProjectForm()

    return render(request, 'admin_panel/project_management.html', {'projects': projects, 'form': form})

@user_passes_test(is_superadmin)
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, "❌ پروژه با موفقیت حذف شد!")
    return redirect('project-management')
