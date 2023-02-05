from django.db import models

from django.contrib.auth.models import User


ANIMAL_CHOICES = (
    ("Male","Male"),
    ("Female", "Female")
)

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class AnimalBreed(TimeStamp):
    animal_breed = models.CharField(max_length=100)
      
    def __str__(self):
        return f"{self.animal_breed}"

class AnimalColor(TimeStamp):
    animal_color = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.animal_color}"

class AnimalCategory(TimeStamp):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.animal_category}"

class Animal(TimeStamp):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE, related_name='animals_category')
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=1)
    gender = models.CharField(max_length=50, choices=ANIMAL_CHOICES)
    color = models.ManyToManyField(AnimalColor, null=True)
    breed = models.ManyToManyField(AnimalBreed, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class AnimalLocation(TimeStamp):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='location')
    location = models.CharField(max_length=255)
    
class AnimalImage(TimeStamp):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Animals')
    
    
    
    