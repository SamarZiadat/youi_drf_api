from django.db import models
from django.contrib.auth.models import User
from events.models import Event

RATINGS = (
    ("5 stars", "5 stars"),
    ("4 stars", "4 stars"),
    ("3 stars", "3 stars"),
    ("2 stars", "2 stars"),
    ("1 star", "1 star"),
    ("0 stars", "0 stars"),
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
