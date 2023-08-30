from django.urls import path, include
from rest_framework import routers
from .views import LocationViewSet, AdViewSet , DailyReportListView ,DailyLocationReportView

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'ads', AdViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('daily-report/<str:report_date>/', DailyReportListView.as_view(), name='daily_report'),
    path('daily-report/', DailyLocationReportView.as_view(), name='all_dates'), 
]