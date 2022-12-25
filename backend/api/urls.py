from django.urls import include
from django.urls import path

from backend.core.yasg import urlpatterns as doc_urlpatterns

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_urlpatterns
