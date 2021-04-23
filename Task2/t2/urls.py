
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page, name="login"),
    path('login/', views.login_page, name="login"),
    path('registration/', views.registration, name="registration"),
    path('user_form/', views.user_form, name="update"),
    path('user/<str:pk_test>/', views.user, name="user"),
    path('logout/',views.logoutUser,name='logoutuser'),
    path('search/',views.search,name='search'),
    
]
