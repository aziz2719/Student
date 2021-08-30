from django.urls import path
from users.views import StudentView, StudentImageView


urlpatterns = [
    path('student/', StudentView.as_view({'get': 'list', 'post': 'create'})),
    path('student/<int:pk>/', StudentView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
    path('image/', StudentImageView.as_view({'get': 'list', 'post': 'create'})),
    path('image/<int:pk>/', StudentImageView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
]