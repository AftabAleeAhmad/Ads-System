from django.db import models
from django.utils import timezone

class Location(models.Model):
    loc_name = models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name
    

class Ad(models.Model):
    ad_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ManyToManyField(Location)
    image = models.ImageField(upload_to='ad_pictures', null=True)
    def __str__(self) -> str:
        return self.ad_name

class VisitorCount(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.count} - {self.location}"

class DailyLocationReport(models.Model):
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey('Ads_app.Location', on_delete=models.CASCADE)
    visitor_count = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.location.loc_name}"



def increment_visitor_count(location):
    """
    Increments the visitor count for a given location.

    Parameters:
    - location: The location for which the visitor count needs to be incremented. (Type: str)

    Return:
    - None
    """
    today = timezone.now().date()
    visitor_count, created = VisitorCount.objects.get_or_create(location=location, date=today)
    visitor_count.count += 1
    visitor_count.save()

def check_visitor_limit(ad, location):
    """
    Check if the visitor limit has been reached for a given ad and location.

    Args:
        ad (Ad): The ad to check the visitor limit for.
        location (Location): The location to check the visitor limit for.

    Returns:
        bool: True if the visitor limit has not been reached, False otherwise.
    """
    today = timezone.now().date()
    visitor_count = VisitorCount.objects.get(location=location, date=today)
    max_visitors = 0
    if location.loc_name == 'Karachi':
        max_visitors = 200
    elif location.loc_name == 'Lahore':
        max_visitors = 100
    elif location.loc_name == 'Multan':
        max_visitors = 1000

    if visitor_count.count >= max_visitors:
        # Blocking ad for this location
        ad.locations.remove(location)
        ad.save()
        return False

    return True

def unblock_ads():
    """
    Unblock ads that have not yet reached their end date.

    This function retrieves the current date and filters the `Ad` objects based on their end date.
    For each `Ad` object in the filtered queryset, the `locations` attribute is updated to include all
    available `Location` objects. Finally, the changes are saved to the database.

    Parameters:
        None

    Returns:
        None
    """
    today = timezone.now().date()
    ads_to_unblock = Ad.objects.filter(end_date__gte=today)
    for ad in ads_to_unblock:
        ad.locations.set(Location.objects.all())
        ad.save()
