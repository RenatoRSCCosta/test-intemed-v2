from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from apps.schedule.views import ScheduleViewSet
from apps.consultation.views import ConsultationViewSet

router = routers.DefaultRouter()
router.register('schedules', ScheduleViewSet, basename="schedules")
router.register('consultations', ConsultationViewSet, basename="consultations")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', include('swagger.urls')),
    path('', include(router.urls)),
]
