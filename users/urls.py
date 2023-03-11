from rest_framework.routers import DefaultRouter
from .views import BusinessOwnerViewSet


router = DefaultRouter()

router.register('business_owner', BusinessOwnerViewSet, basename='business_owner')



urlpatterns = router.urls
