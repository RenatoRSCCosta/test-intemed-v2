from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from apps.schedule.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register('schedules', ScheduleViewSet, basename="schedule")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('schedules/', ScheduleViewSet.as_view()),
    path('', include(router.urls)),
]
