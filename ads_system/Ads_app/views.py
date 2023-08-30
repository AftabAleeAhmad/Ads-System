from rest_framework import viewsets
from .models import Ad, Location, DailyLocationReport
from .serializers import AdSerializer, LocationSerializer
from django.views.generic import ListView , TemplateView

# Create your views here.

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class DailyReportListView(ListView):
    model = DailyLocationReport
    template_name = 'Ads_app/report.html'
    context_object_name = 'daily_reports'

    def get_queryset(self):
        """
        Retrieves the queryset of DailyLocationReport objects based on the provided report date.

        Parameters:
            self: The instance of the class.
        
        Returns:
            A queryset of DailyLocationReport objects filtered by the specified report date.
        """
        report_date = self.kwargs['report_date']
        print(report_date)
        return DailyLocationReport.objects.filter(date=report_date)
        

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :param kwargs: Additional keyword arguments.
        :return: The context data with the report date added.
        """
        context = super().get_context_data(**kwargs)
        context['report_date'] = self.kwargs['report_date']
        return context


class DailyLocationReportView(TemplateView):
    template_name = "Ads_app/all_dates.html"
    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.
        
        :param kwargs: Keyword arguments passed to the function.
        :return: The context data with the "date_list" attribute added.
        """
        date_list = DailyLocationReport.objects.values_list('date__year','date__month','date__day')
        date_list = [f"{year}-{month}-{day}" for year, month, day in date_list]
        print(date_list)
        context = super().get_context_data(**kwargs)
        context["date_list"] = date_list
        return context
    
    