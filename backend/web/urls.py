from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name="url_mainpage"),

    path('login/', views.LoginUserView.as_view(), name="url_login"),
    path('logout/', views.LogoutUserView.as_view(), name="url_logout"),
    path('signup/', views.SignupUserView.as_view(), name="url_signup"),

    path('messages/', include('sms.urls'), name="url_messages"),
]