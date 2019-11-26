from django.urls import path
from .views import IndexView, DestinationDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination'),
]
