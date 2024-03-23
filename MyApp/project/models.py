from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
    
class Project(models.Model):

    CHOICES = [
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
        ('Postponed','Postponed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(choices=CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

class Task(models.Model):
    description = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'