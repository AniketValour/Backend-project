from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from itemsapp.views import ItemViewSet  # Changed from myapp to itemsapp

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]