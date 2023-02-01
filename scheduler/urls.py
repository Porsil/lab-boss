from . import views
from django.urls import path


urlpatterns = [
     path('scheduler', views.WorkloadList.as_view(), name='scheduler'),
     path('workload/<pk>/update/', views.UpdateWorkload.as_view(),
          name='update_workload'),
     path('workload/<pk>/delete/', views.DeleteWorkload.as_view(),
          name='delete_workload'),
     path('analysts', views.AnalystList.as_view(), name='analysts'),
     path('analysts/add', views.AddAnalyst.as_view(), name='add_analyst'),
     path('analysts/<pk>/update/', views.UpdateAnalyst.as_view(),
          name='update_analyst'),
     path('analysts/<pk>/delete/', views.DeleteAnalyst.as_view(),
          name='delete_analyst'),
     path('toggle_analyst/<pk>', views.ToggleAnalyst.as_view(),
          name='toggle_analyst'),
     path('tests', views.TestList.as_view(), name='tests'),
     path('tests/add', views.AddTest.as_view(), name='add_test'),
     path('tests/<pk>/update/', views.UpdateTest.as_view(),
          name='update_test'),
     path('tests/<pk>/delete/', views.DeleteTest.as_view(),
          name='delete_test'),
     path('toggle_test/<pk>', views.ToggleTest.as_view(),
          name='toggle_test'),
]
