from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from apps.schedule.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register('schedule', ScheduleViewSet, basename="schedules")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('schedules/', ScheduleList.as_view()),
    path('', include(router.urls)),
]
