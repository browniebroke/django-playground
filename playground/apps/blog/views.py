from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from playground.apps.blog.models import Property, Item
from playground.apps.blog.serializers import PropertySerializer, ItemSerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permissions_classes = [IsAuthenticated]


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permissions_classes = [IsAuthenticated]