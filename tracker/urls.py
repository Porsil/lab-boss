from . import views
from django.urls import path
from .views import DeleteMaterial


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('materials', views.MaterialList.as_view(), name='materials'),
    path('tracker', views.BatchList.as_view(), name='tracker'),
    path('materials/<pk>/delete/', DeleteMaterial.as_view(), name='delete_material'),
]