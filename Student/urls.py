from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    path('user/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
