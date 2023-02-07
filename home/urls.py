from django.urls import path

from .views import (
    AnimalList,
    AnimalDetail
)
urlpatterns = [
    path('list/', AnimalList.as_view(), name='animal-list'),
    path('list/<int:pk>/', AnimalDetail.as_view(), name='animal-detail')
]