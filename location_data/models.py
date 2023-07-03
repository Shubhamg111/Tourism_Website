from django.db import models

# Create your models here.
province=(
    ("Sudurpaschim","Sudurpaschim"),
    ("Karnali Province","Karnali Province"),
    ("Lumbini Province","Lumbini Province"),
    ("Gandaki Province","Gandaki Province"),
    ("Bagmati Province","Bagmati Province"),
    ("Madesh Province","Madesh Province"),
    ("Province 1","Province 1"),
)
# hi I tried to remove the tuples and made the Province model as foreign key in district but coudn't and
# it keep showing errors. I don't know how to fix that so tuples and Province models are existing side by side as
#  the data in Province model matches the tuple and changing any of them will cause errors. It works for now show let it be.
class Province(models.Model):
    province_name=models.CharField(max_length=100)
    province_desc=models.TextField()
    province_images=models.FileField(upload_to='static/uploads/province')

    def __str__(self):
        return self.province_name

class District(models.Model):
    province=models.CharField(max_length=100,choices=province)
    district_name=models.CharField(max_length=100)
    district_desc=models.TextField()
    district_images = models.FileField(upload_to='static/uploads')

    def __str__(self):
        return self.district_name



class Events(models.Model):
    event_name=models.CharField(max_length=100)
    event_desc=models.TextField()
    event_image=models.FileField(upload_to='static/uploads/events',null=True)
    event_date=models.DateField()

    def __str__(self):
        return self.event_name


class Location(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    location_name=models.CharField(max_length=100)
    location_desc=models.TextField()
    location_image = models.FileField(upload_to='static/uploads/location',null=True)
    best_season = models.CharField(max_length=10, default='any', choices=(('any', 'any'), ('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter')))
    # event=models.ForeignKey(Events, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.location_name
    




