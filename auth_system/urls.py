from django.urls import path

from auth_system import views


urlpatterns = [
    path('register-page/', views.register_page, name='register'),
    path('login-page/', views.login_page, name='login'),
    path('logout-page/', views.logout_page, name='logout'),

]