from . import views
from django.urls import path
from .views import AddMaterial, UpdateMaterial, DeleteMaterial
from .views import UpdateBatch, DeleteBatch


urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('materials', views.MaterialList.as_view(), name='materials'),
     path('tracker', views.BatchList.as_view(), name='tracker'),
     path('materials/<pk>/delete/', DeleteMaterial.as_view(),
          name='delete_material'),
     path('materials/<pk>/update/', UpdateMaterial.as_view(),
          name='update_material'),
     path('materials/add', AddMaterial.as_view(), name='add_material'),
     path('tracker/<pk>/delete/', DeleteBatch.as_view(), name='delete_batch'),
     path('tracker/<pk>/update/', UpdateBatch.as_view(),
          name='update_batch'),
]
