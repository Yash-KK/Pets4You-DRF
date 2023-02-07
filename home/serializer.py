from rest_framework import serializers

#DJANGO
from .models import (
    AnimalBreed,
    AnimalColor,
    AnimalCategory,
    
    Animal,
    
    AnimalImage,
    AnimalLocation    
)

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalBreed
        fields = ['animal_breed']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalColor
        fields = ['animal_color']

class CateogrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalCategory
        fields = '__all__'
        
class AnimalSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    breed = BreedSerializer(many=True)
    color = ColorSerializer(many=True)
    
    class Meta:
        model = Animal
        exclude = ['slug', 'modified_at']

    def get_category(self, obj):
        return f"{obj.category.category}"
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocation
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImage
        fields ='__all__'
    