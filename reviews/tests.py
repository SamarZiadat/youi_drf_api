from django.contrib.auth.models import User
from .models import Event
from .models import Review
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewsListViewTests(APITestCase):
    """
    Tests for the Review model list view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        event_a = Event.objects.create(
            owner=samar, description="an event", event_date="2024-04-01"
        )

    def test_can_list_reviews(self):
        samar = User.objects.get(username="samar")
        event_a = Event.objects.get(id=1)
        Review.objects.create(owner=samar, event=event_a, review="a review", rating="5")
        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReviewsDetailViewTests(APITestCase):
    """
    Tests for the Review model detail view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        event_a = Event.objects.create(
            owner=samar, description="an informative event", event_date="2025-04-01"
        )
        event_b = Event.objects.create(
            owner=charlotte,
            description="a less informative event",
            event_date="2026-04-01",
        )

    def test_cant_retrieve_review_using_invalid_id(self):
        response = self.client.get("/reviews/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
