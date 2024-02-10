from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from web import views

# url('^accounts/', include('django.contrib.auth.urls'))

urlpatterns = [
    path('', views.main_view, name="main"),
    path('registration/', views.registration_view, name="registration"),
    path('auth/', views.auth_view, name="auth"),
    path('logout/', views.logout_view, name="logout"),
    path('sessions/', views.sessions_view, name="sessions_view"),
    path('session/add', views.session_edit_view, name="add_session"),
    path('session/<int:id>', views.session_edit_view, name="edit_session"),
    path('session/<int:id>/delete', views.session_delete_view, name="delete_session"),
    path("symptoms/", views.symptoms_view, name="symptoms"),
    path("symtoms/<int:id>/delete/", views.symptoms_delete_view, name="symptoms_delete"),
    path("massages/", views.massage_types_view, name="massages"),
    path("massages/<int:id>/delete/", views.massage_types_delete_view, name="massages_delete")
]
