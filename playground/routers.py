from rest_framework.routers import DefaultRouter

from playground.apps.blog.views import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")

app_name = "api"
urlpatterns = router.urls
