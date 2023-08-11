from django.urls import path
from .views import *

urlpatterns = [
    path('unit/',unit,name='unit'),
    path('visit/<int:pk>',visit,name='visit'),
]