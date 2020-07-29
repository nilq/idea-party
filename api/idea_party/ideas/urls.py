from django.urls import path

from . import views

urlpatterns = [
    path('', views.ideas),
    path('idea/', views.idea, name='idea'),
]