from django.urls import path

from .views import index

app_name = 'portfolio'
urlpatterns = [
    path('', view=index, name='index'),
]
