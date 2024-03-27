from django.urls import path
from .views import convert_to_pdf

urlpatterns = [
    path('', convert_to_pdf, name='convert'),

]
