from django.shortcuts import render

def projects(request):
    return render(request, 'projects/projects_list.html')