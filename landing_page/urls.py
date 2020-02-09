from django.urls import path, include
from rest_framework import routers
from .views import index_view, MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', index_view, name='index'),
    path('api/', include(router.urls)),
]
