from . import views
from django.urls import path


urlpatterns = [
     path('analysts', views.AnalystList.as_view(), name='analysts'),
     path('analysts/add', views.AddAnalyst.as_view(), name='add_analyst'),
]
