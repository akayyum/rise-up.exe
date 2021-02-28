from django.urls import path
from . import views

urlpatterns = [

    path('', views.mentor, name='mentor'),
    path('home/', views.mentor, name='mentor'),
    path('guidance/', views.guidance, name='guidance'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('reg/', views.registerPage, name="reg"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]