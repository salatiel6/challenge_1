from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from customer_base.views import ClientsViewSet

router = routers.DefaultRouter()
router.register('clients', ClientsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
