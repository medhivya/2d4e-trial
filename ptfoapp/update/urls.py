from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:printer_id>/', views.status, name = "status"),
    path('<int:printer_id>/update/', views.newUpdate, name = "newUpdate")
]
