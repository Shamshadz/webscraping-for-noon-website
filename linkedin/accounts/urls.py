from django.urls import path
from accounts import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]