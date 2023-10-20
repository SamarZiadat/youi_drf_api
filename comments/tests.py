from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentsListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        post_a = Post.objects.create(owner=samar, content="a post")

    def test_can_list_comments(self):
        samar = User.objects.get(username="samar")
        post_a = Post.objects.get(id=1)
        Comment.objects.create(owner=samar, post=post_a, content="a comment")
        response = self.client.get("/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentsDetailViewTests(APITestCase):
    """
    Tests for the Comment model detail view
    """

    def setUp(self):
        samar = User.objects.create_user(username="samar", password="letmein")
        charlotte = User.objects.create_user(username="charlotte", password="pass")
        post_a = Post.objects.create(owner=samar, content="an informative post")
        post_b = Post.objects.create(owner=charlotte, content="a less informative post")

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get("/comments/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
