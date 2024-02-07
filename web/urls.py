from django.urls import path

from web import views

urlpatterns = [
    path('', views.main_view, name="main"),
    path('stat/', views.stat_view, name="stat"),
    path('analytics/', views.analytics_view, name="analytics"),
    path('registration/', views.registration_view, name="registration"),
    path('auth/', views.auth_view, name="auth"),
    path('logout/', views.logout_view, name="logout"),
    path('session/add', views.session_edit_view, name="add_session"),
    path('session/<int:id>', views.session_edit_view, name="edit_session"),
    path('session/<int:id>/delete', views.session_delete_view, name="delete_session"),
    path("symptoms/", views.symptoms_view, name="symptoms"),
    path("symtoms/<int:id>/delete/", views.symptoms_delete_view, name="symptoms_delete"),
    path("massages/", views.massage_types_view, name="massages"),
    path("massages/<int:id>/delete/", views.massage_types_delete_view, name="massages_delete"),
]