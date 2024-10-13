from django.urls import path
from . import views
from .views import user_login  

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]
