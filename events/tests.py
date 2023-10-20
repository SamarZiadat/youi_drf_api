from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """

    def setUp(self):
        User.objects.create_user(username="samar", password="letmein")

    def test_can_list_events(self):
        samar = User.objects.get(username="samar")
        Event.objects.create(owner=samar, title="event title", event_date="2024-04-01")
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventDetailViewTests(APITestCase):
    """
    Tests for the Event model detail view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        Event.objects.create(
            owner=samar,
            title="a title",
            description="samar's event",
            tags="tag",
            event_date="2024-04-01",
        )
        Event.objects.create(
            owner=charlotte,
            title="another title",
            description="charlotte's content",
            tags="tag",
            event_date="2025-04-01",
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get("/events/1/")
        self.assertEqual(response.data["title"], "a title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get("/events/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)