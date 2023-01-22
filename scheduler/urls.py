from . import views
from django.urls import path


urlpatterns = [
     path('analysts', views.AnalystList.as_view(), name='analysts'),
]
