from django.urls import path

from accounts import views

urlpatterns = [
    path('user/login/', views.user_login, name='user-login'),

]

