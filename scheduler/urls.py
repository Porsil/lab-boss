from . import views
from django.urls import path


urlpatterns = [
     path('analysts', views.AnalystList.as_view(), name='analysts'),
     path('analysts/add', views.AddAnalyst.as_view(), name='add_analyst'),
     path('analysts/<pk>/update/', views.UpdateAnalyst.as_view(),
          name='update_analyst'),
     path('analysts/<pk>/delete/', views.DeleteAnalyst.as_view(),
          name='delete_analyst'),
     path('tests', views.TestList.as_view(), name='tests'),
     path('tests/add', views.AddTest.as_view(), name='add_test'),
     path('tests/<pk>/update/', views.UpdateTest.as_view(),
          name='update_test'),
     path('tests/<pk>/delete/', views.DeleteTest.as_view(),
          name='delete_test'),
]
