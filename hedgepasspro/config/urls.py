from django.contrib import admin
from django.urls import path, include  # Import include to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include main app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  
]

