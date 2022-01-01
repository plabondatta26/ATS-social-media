from django.urls import path, include
from rest_framework import routers
from .views import *
router= routers.DefaultRouter()
router.register('user/create', UserCreationViewSet, basename='account_apis')

urlpatterns = [
    path('api/', include(router.urls)),

]
