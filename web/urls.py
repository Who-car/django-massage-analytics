from django.urls import path

from web import views

urlpatterns = [
    path('', views.main_view, name="main"),
    path('registration/', views.registration_view, name="registration"),
    path('auth/', views.auth_view, name="auth"),
    path('logout/', views.logout_view, name="logout")
]