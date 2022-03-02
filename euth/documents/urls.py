from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ParagraphDetailView.as_view(),
         name='paragraph-detail'),
]
