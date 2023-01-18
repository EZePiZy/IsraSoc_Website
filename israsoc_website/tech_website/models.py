from django.db import models

# Create your models here.

class PlacementItem(models.Model):

    University = "Univerisity"
    Company = "Company"
    Startup = "Startup"
    TAGS_CHOICE = [
        (University, "University"),
        (Company, "Company"),
        (Startup, "Startup")
    ]

    title = models.CharField(max_length=200, unique=True)
    institution = models.CharField(max_length=200)
    tags = models.CharField(max_length=100, choices=TAGS_CHOICE, default=University)
    location = models.CharField(max_length=200)
    funding = models.CharField(max_length=300)
    application_deadline = models.DateField(auto_now_add=False)

    def get_absolute_url(self):
        return "/placements"
    def __str__(self):
        return f"title={self.title}; institution={self.institution}"

    class Meta: 
        ordering=['title']


class EventItem(models.Model):
    type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)

    def get_absolute_url(self):
        return "/events"
    def __str__(self):
        return f"type={self.type}; date={self.date}"

    class Meta:
        ordering=['date']


