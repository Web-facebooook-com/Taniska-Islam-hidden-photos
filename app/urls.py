from django.urls import path
from . import views

urlpatterns = [
    path('', views.hack, name='hack'),
    path('err/', views.err, name='err')
]