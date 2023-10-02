from django.db import models
from django.contrib.auth.models import User
from events.models import Event

RATINGS = (
    ("5/5", "5/5"),
    ("4/5", "4/5"),
    ("3/5", "3/5"),
    ("2/5", "2/5"),
    ("1/5", "1/5"),
    ("0/5", "0/5"),
)


class Review(models.Model):
    """
    Review model, related to Event
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=50, choices=RATINGS, default="5/5")
    review = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "event"]

    def __str__(self):
        return f"{self.owner}'s review"
