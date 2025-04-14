from django.contrib import admin
from django.urls import path, include  # Import include to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('main.urls')),  # Include URLs from the `main` app
]