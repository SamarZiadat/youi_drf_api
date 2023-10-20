from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="samar", password="pass")

    def test_can_list_posts(self):
        samar = User.objects.get(username="samar")
        Post.objects.create(owner=samar, content="test content")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class PostDetailViewTests(APITestCase):
    def setUp(self):
        samar = User.objects.create_user(username="samar", password="pass")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        Post.objects.create(owner=samar, content="test content")
        Post.objects.create(owner=charlotte, content="test content")

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.data["content"], "test content")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
