from django.urls import path

from . import views

urlpatterns = [
    path('', views.ideas),
    path('<str:idea_id>/', views.idea, name='idea'),
]