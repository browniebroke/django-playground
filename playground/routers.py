from rest_framework.routers import DefaultRouter

from playground.apps.blog.views import PropertyViewSet, ItemViewSet

router = DefaultRouter()
router.register('property', PropertyViewSet, 'property')
router.register('item', ItemViewSet, 'item')

app_name = "api"
urlpatterns = router.urls
