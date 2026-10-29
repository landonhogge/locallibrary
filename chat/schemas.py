from datetime import datetime, timedelta
from typing import Annotated

from django.db.models import Q
from django.utils import timezone
from ninja import Field, FilterLookup, FilterSchema, ModelSchema, Schema

from .models import Message, Room


class RoomIn(ModelSchema):
    class Meta:
        model = Room
        fields = ["name", "topic"]


class RoomOut(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "name", "topic", "created_at"]


class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = ["content"]


class MessageOut(ModelSchema):
    room: RoomOut

    class Meta:
        model = Message
        fields = ["id", "author", "content", "created_at"]


class Conflict(Schema):
    message: str
    existing_id: int


class RoomFilter(FilterSchema):
    search: str | None = Field(None, q="name__icontains")
    topic: str | None = Field(None, q="topic__icontains")
    recent: bool | None = None

    def filter_recent(self, value: bool) -> Q:
        cutoff = timezone.now() - timedelta(days=7)
        if value:
            return Q(created_at__gte=cutoff)
        return Q(created_at__lt=cutoff)