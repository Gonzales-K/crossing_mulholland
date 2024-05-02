from django.urls import path
from . import views

urlpatterns = [
        # prefix, viewsDir.functionName, alias
    path('', views.index, name='index'),
]