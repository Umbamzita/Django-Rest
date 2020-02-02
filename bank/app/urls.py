from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app import views



router = DefaultRouter()

router.register('customer', views.CustomerViewSet)
router.register('account', views.AccountViewSet)
router.register('action', views.ActionViewSet)



urlpatterns = router.urls 

