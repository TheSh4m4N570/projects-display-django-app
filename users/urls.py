from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name= 'register'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:username>', views.profile, name='profile')
]
