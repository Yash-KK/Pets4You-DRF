from rest_framework import serializers
from django.contrib.auth.models import User

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
        fields = ['category']
        
class AnimalSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner.username')
    category = CateogrySerializer()
    breed = BreedSerializer(many=True)
    color = ColorSerializer(many=True)
    
    class Meta:
        model = Animal
        exclude = ['slug', 'modified_at']

    def validate(self, data):
            
            if 'name' in data:
                name = data['name']
            if 'category' in data:
                category = data['category']['category']
                
                category_instance = AnimalCategory.objects.get(category=category)                
    
                # If same name of the dog exists, then raise an error
                if Animal.objects.filter(name=name, category=category_instance).exists():               
                    raise serializers.ValidationError("Animal name in this category already exists")
            
            return data

    
    def create(self, validated_data):
        category = validated_data.pop('category')['category']
        animal_breed = validated_data.pop('breed')
        animal_color = validated_data.pop('color')
        user = validated_data.pop('owner')['username']
                
        category_instance = AnimalCategory.objects.get(category=category)
        animal = Animal.objects.create(**validated_data, category=category_instance, owner=user)
        
        for breed in animal_breed:
            b = AnimalBreed.objects.get(animal_breed= breed['animal_breed'])
            animal.breed.add(b)
        
        for color in animal_color:
            c = AnimalColor.objects.get(animal_color = color['animal_color'])
            animal.color.add(c)
        
        animal.save()
        return animal
    
    def update(self, instance, validated_data):        
        if 'color' in validated_data:
                instance.color.clear()
                animal_color = validated_data['color']
                for color in animal_color:
                    c = AnimalColor.objects.get(animal_color=color['animal_color'])
                    instance.color.add(c)
        if 'breed' in validated_data:
                instance.breed.clear()
                animal_breed = validated_data['breed']
                for breed in animal_breed:
                    c = AnimalBreed.objects.get(animal_breed=breed['animal_breed'])
                    instance.breed.add(c)                
    
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.gender = validated_data.get('gender', instance.gender)
        return instance
    
    def get_category(self, obj):
        return f"{obj.category.category}"
    
    def get_owner(self, obj):
        return f"{obj.owner.username}"
  
        
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocation
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalImage
        fields ='__all__'
    