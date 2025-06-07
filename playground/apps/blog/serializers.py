import copy

from rest_framework import serializers

from playground.apps.blog.models import Item, Property


class PropertySerializer(serializers.Serializer):
    name = serializers.CharField()

class ItemSerializer(serializers.ModelSerializer):

    properties = PropertySerializer(many=True, required=False)

    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        data = copy.deepcopy(validated_data)
        properties = data.pop("properties", [])
        item = Item.objects.create(**data)
        for property in properties:
            current_property, _ = Property.objects.get_or_create(**property)
            item.properties.add(current_property)
        return item