from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('materials', views.MaterialList.as_view(), name='materials'),
    path('tracker', views.BatchList.as_view(), name='tracker'),
]