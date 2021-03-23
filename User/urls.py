from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user-signup', SignUpViewSet, basename = "signup")

urlpatterns = router.urls
