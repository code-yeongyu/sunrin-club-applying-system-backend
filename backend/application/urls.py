from django.urls import path
from application import views

urlpatterns = [
    path('apply/',
         views.ApplicationCreation.as_view(),
         name='ApplicationCreation'),
    path('<int:pk>/',
         views.ApplicationDetail.as_view(),
         name='ApplicationDetail'),
    path('', views.applications_list, name='applications_view'),
]
