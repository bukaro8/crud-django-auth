from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.log_in, name='login'),
    path('profile/', views.tasks, name='profile'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.tasks, name='logout'),
    path('accounts/profile/', views.profile, name='profile'),

]
