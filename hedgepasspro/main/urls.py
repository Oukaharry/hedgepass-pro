from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  # Import auth_views for authentication views
from django.contrib.auth.views import LogoutView  # Import LogoutView for logout functionality
from . import views  # Import views from the main app

app_name = 'main'  # Define the app name for namespacing

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page first
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-account/', views.add_account, name='add_account'),
    path('pairs/', views.view_pairs, name='view_pairs'),
    path('', views.landing, name='landing'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),  # Signup page
    path('client_area/', views.client_area, name='client_area'),  # Client area
    path('account_management/', views.account_management, name='account_management'),  # Account management
    path('performance/', views.performance, name='performance'),  # Performance page
    path('portfolio_performance/', views.portfolio_performance, name='portfolio_performance'),  # Portfolio performance
    path('settings/', views.settings, name='settings'),  # Settings page
    path('delete_account/', views.delete_account, name='delete_account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.custom_logout, name='logout'),  # Use the custom logout view
]