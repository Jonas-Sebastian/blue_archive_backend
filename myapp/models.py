from django.db import models

class TotalAssault(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class GrandAssault(models.Model):
    COLOR_CHOICES = [
        ('Red', 'Explosive'),
        ('Yellow', 'Piercing'),
        ('Blue', 'Mystic'),
        ('Purple', 'Sonic'),
        ('Normal', 'Normal'),
    ]

    name = models.CharField(max_length=200)
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='Normal',  # Set 'Normal' as the default value
    )

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    #Changes how the name appears in Django Admin
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, related_name='students', blank=True)
    total_assaults = models.ManyToManyField(TotalAssault, related_name='students_total_assault', blank=True)
    grand_assaults = models.ManyToManyField(GrandAssault, related_name='students_grand_assault', blank=True)

    def __str__(self):
        return self.name