from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.schedule.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register('schedule', ScheduleViewSet, basename="schedules")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
