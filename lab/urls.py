from django.urls import path
from .import views

app_name = 'lab'

urlpatterns = [
    path('', views.LabListView.as_view(), name='lab-list'),
    path('<int:pk>/', views.LabDetailView.as_view(), name='lab-detail'),
    path('<int:pk>/<str:item_name>/', views.LabItemsListView.as_view(), name='lab-items-list'),
]