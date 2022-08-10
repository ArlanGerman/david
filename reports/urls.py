from django.contrib import admin
from django.urls import path

from reports.views import ReportsListCreateAPIView, ReportsRetrieveUpdateDestroyRetrieveAPIView

urlpatterns = [
    path('reports/', ReportsListCreateAPIView.as_view()),
    path('reports/<int:pk>/', ReportsRetrieveUpdateDestroyRetrieveAPIView.as_view())
]