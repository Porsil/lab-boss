from . import views
from django.urls import path


urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('materials', views.MaterialList.as_view(), name='materials'),
     path('materials/add', views.AddMaterial.as_view(), name='add_material'),
     path('materials/<pk>/update/', views.UpdateMaterial.as_view(),
          name='update_material'),
     path('materials/<pk>/delete/', views.DeleteMaterial.as_view(),
          name='delete_material'),
     path('tracker', views.BatchList.as_view(), name='tracker'),
     path('toggle/<pk>', views.ToggleMaterial.as_view(), name='toggle'),
     path('tracker/add', views.AddBatch.as_view(), name='add_batch'),
     path('tracker/<pk>/update/', views.UpdateBatch.as_view(),
          name='update_batch'),
     path('tracker/<pk>/delete/', views.DeleteBatch.as_view(),
          name='delete_batch'),
]
