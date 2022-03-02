from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.OfflineEventDetailView.as_view(),
         name='offlineevent-detail'),
]
