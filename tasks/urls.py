from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
