from django.urls import path
from .views import *

urlpatterns = [
    path('check/',CheckTasks.as_view(),name="check"),
]
