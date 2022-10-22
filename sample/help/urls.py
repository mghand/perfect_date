from django.urls import path

from help import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('help/create/', views.CreateReqView.as_view(), name='req-create'),
    path('help/', views.ListReqView.as_view(), name='req-list'),
]
