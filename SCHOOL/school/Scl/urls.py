from django.urls import path
from .import views
urlpatterns=[
    # path('', views.base, name=''),
    path('',views.home ,name='home'),
    path('attendance',views.attendance, name='attendance'),
    path('login',views.login ,name='login'),
    path('register',views.register ,name='register'),
    path('view_attendance',views.show_attnd,name='show_attnd'),
]