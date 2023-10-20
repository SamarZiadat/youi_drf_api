from django.contrib.auth.models import User
from .models import Event
from .models import Bookmark
from rest_framework import status
from rest_framework.test import APITestCase


class BookmarkListViewTests(APITestCase):
    """
    Tests for the Bookmark model list view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        event_a = Event.objects.create(
            owner=samar, title="an informative event", event_date="2030-04-01"
        )

    def test_can_list_bookmark(self):
        samar = User.objects.get(username="samar")
        event_a = Event.objects.get(id=1)
        Bookmark.objects.create(owner=samar, event=event_a)
        response = self.client.get("/bookmarks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class BookmarkDetailViewTests(APITestCase):
    """
    Tests for the Bookmark model detail view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        event_a = Event.objects.create(
            owner=samar, title="an informative event", event_date="2030-04-01"
        )
        event_b = Event.objects.create(
            owner=charlotte, title="a less informative event", event_date="2030-04-01"
        )
        Bookmark.objects.create(owner=samar, event=event_a)
        Bookmark.objects.create(owner=charlotte, event=event_b)

    def test_cant_retrieve_bookmark_using_invalid_id(self):
        response = self.client.get("/bookmarks/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_bookmark_using_valid_id(self):
        response = self.client.get("/bookmarks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
