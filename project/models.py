from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('remodeling', 'Remodeling'),
        ('construction', 'Construction'),
        ('repairs', 'Repairs'),
        ('design', 'Design'),
    ]
    
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='projects/',null=True)
    created_at = models.DateField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)

    def __str__(self):
        return self.title
