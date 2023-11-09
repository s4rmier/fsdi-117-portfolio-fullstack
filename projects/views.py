from django.shortcuts import render
from .forms import ProjectForm
def projects(request):
    return render(request, 'projects/projects_list.html')

#Homework

# def project_new(request):
#     #create an instance of the form
#     #render the instance to the html
def project_new(request):
    form = ProjectForm()

    return render(request, 'projects/projects_new.html', {
        'form': form
    })