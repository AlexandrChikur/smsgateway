from django.urls import include
from django.urls import path

from core.yasg import urlpatterns as doc_urlpatterns
from sms import api as sms_api_view

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),

    path('messages/', sms_api_view.MessageAPIView.as_view()),
]

urlpatterns += doc_urlpatterns
