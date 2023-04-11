from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_user_view),
]