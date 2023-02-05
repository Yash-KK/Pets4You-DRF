# Generated by Django 4.1.6 on 2023-02-05 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=1)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('animal_breed', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('animal_color', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=255)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='home.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='Animals')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ManyToManyField(null=True, to='home.animalbreed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals_category', to='home.animalcategory'),
        ),
        migrations.AddField(
            model_name='animal',
            name='color',
            field=models.ManyToManyField(null=True, to='home.animalcolor'),
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
    ]