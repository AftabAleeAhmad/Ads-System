import schedule
import time
from datetime import datetime
from .models import DailyLocationReport,Location , VisitorCount, unblock_ads

def generate_daily_report():
    """
    Generates a daily report by calculating the visitor count for each location on the current date.

    Parameters:
        None

    Returns:
        None
    """
    report_date = datetime.now().date()
    locations = Location.objects.all()
    for location in locations:
        visitor_count = VisitorCount.objects.get(location=location, date=report_date)
        daily_report = DailyLocationReport(date=report_date, location=location, visitor_count=visitor_count)
        daily_report.save()

schedule.every().day.at("11:59:59").do(generate_daily_report)
schedule.every().day.at('00:00').do(unblock_ads)

while True:
    schedule.run_pending()
    time.sleep(1)
