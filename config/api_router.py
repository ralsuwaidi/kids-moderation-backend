from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from content_moderation.users.api.views import UserViewSet
from content_moderation.moderation.api.views import MovieViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("movie", MovieViewSet)


app_name = "api"
urlpatterns = router.urls
