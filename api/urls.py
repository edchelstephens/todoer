from rest_framework import routers

from django.urls import path, include

from api.serializers.user import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]