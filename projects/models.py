from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='projects_images/')
    repository = models.URLField()
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.name} - ({self.year})"