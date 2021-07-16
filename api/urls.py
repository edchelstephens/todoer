from rest_framework import routers

from django.urls import path, include

from api.serializers.user import UserViewSet
from api.serializers.todo import TodoViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("", include(router.urls))
]