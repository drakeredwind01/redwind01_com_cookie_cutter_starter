from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from redwind01_com_cookie_cutter_starter.users.api.views import UserViewSet
from library.views import BooksViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("Books", BooksViewSet)

app_name = "api"
urlpatterns = router.urls

