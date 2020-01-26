from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='drinks')
router.register(r'workers', WorkerViewSet, basename='workers')
router.register(r'sales', SaleViewSet, basename='sales')

urlpatterns = router.urls
