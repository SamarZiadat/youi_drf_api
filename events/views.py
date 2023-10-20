from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from youi_drf_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    List events or create a event if logged in
    The perform_create method associates the event with the logged in user.
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        bookmarks_count=Count("bookmarks", distinct=True),
        reviews_count=Count("reviews", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        "owner__followed__owner__profile": ["exact"],
        "bookmarks__owner__profile": ["exact"],
        "owner__profile": ["exact"],
        "category": ["exact"],
        "event_date": ["lte"],
    }
    search_fields = [
        "owner__username",
        "title",
        "event_date",
        "tags__name",
    ]
    ordering_fields = [
        "bookmarks_count",
        "reviews_count",
        "bookmarks__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a event and edit or delete it if you own it.
    """

    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        bookmarks_count=Count("bookmarks", distinct=True),
        reviews_count=Count("reviews", distinct=True),
    ).order_by("-created_at")
