from django.db import models
from django.contrib.auth.models import User
from datetime import date
from taggit.managers import TaggableManager

EVENT_CATEGORIES = (
    ("Conference", "Conference"),
    ("Networking", "Networking"),
    ("Panel", "Panel"),
    ("Product launch", "Product launch"),
    ("Talk", "Talk"),
    ("Workshop", "Workshop"),
    ("Other", "Other"),
)

EVENT_FORMATS = (
    ("In person", "In person"),
    ("Hybrid", "Hybrid"),
    ("Online", "Online"),
)


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_date = models.DateField(blank=False)
    tags = TaggableManager(blank=True)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default="Conference"
    )
    format = models.CharField(max_length=50, choices=EVENT_FORMATS, default="In person")
    image = models.ImageField(
        upload_to="images/", default="../default_post_e675n6", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
