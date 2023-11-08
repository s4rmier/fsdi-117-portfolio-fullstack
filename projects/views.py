from django.shortcuts import render

def projects(request):
    return render(request, 'projects/projects_list.html')


#Homework

def project_new(request):
    #create an instance of the form
    #render the instance to the html
    return render(request, 'projects/projects_new.html')