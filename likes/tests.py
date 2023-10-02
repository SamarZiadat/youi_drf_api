from django.contrib.auth.models import User
from .models import Post
from .models import Like
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    """
    Tests for the Like model list view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        post_a = Post.objects.create(owner=samar, content="an informative post")

    def test_can_list_like(self):
        samar = User.objects.get(username="samar")
        post_a = Post.objects.get(id=1)
        Like.objects.create(owner=samar, post=post_a)
        response = self.client.get("/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_like(self):
        post_a = Post.objects.get(id=1)
        response = self.client.post("/likes/", {"post": post_a})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Like.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_post_like(self):
        self.client.login(username="samar", password="letmein")
        post_a = Post.objects.get(id=1)
        current_user = User.objects.get(username="samar")
        response = self.client.post("/likes/", {"owner": current_user, "post": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LikeDetailViewTests(APITestCase):
    """
    Tests for the Like model detail view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        post_a = Post.objects.create(owner=samar, content="an informative post")
        post_b = Post.objects.create(owner=charlotte, content="a less informative post")
        Like.objects.create(owner=samar, post=post_a)
        Like.objects.create(owner=charlotte, post=post_b)

    def test_cant_retrieve_like_using_invalid_id(self):
        response = self.client.get("/likes/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_like_using_valid_id(self):
        response = self.client.get("/likes/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_delete_own_like(self):
        self.client.login(username="samar", password="letmein")
        current_user = User.objects.get(username="samar")
        response = self.client.delete("/likes/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_in_user_cant_delete_someone_elses_like(self):
        self.client.login(username="samar", password="letmein")
        current_user = User.objects.get(username="samar")
        response = self.client.delete("/likes/2/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_post_like_to_the_same_post_twice(self):
        self.client.login(username="samar", password="letmein")
        current_user = User.objects.get(username="samar")
        post_a = Post.objects.get(id=1)
        response = self.client.post("/likes/", {"owner": current_user, "post": 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
