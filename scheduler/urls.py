from . import views
from django.urls import path


urlpatterns = [
    path('analysts', views.AnalystList.as_view(), name='analysts'),
    path('analysts/add', views.AddAnalyst.as_view(), name='add_analyst'),
    path('analysts/<pk>/update/', views.UpdateAnalyst.as_view(),
         name='update_analyst'),
    path('analysts/<pk>/delete/', views.DeleteAnalyst.as_view(),
         name='delete_analyst'),
]
