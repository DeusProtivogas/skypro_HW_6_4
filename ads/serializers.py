
from rest_framework import serializers

from ads.models import Category, Ad, Selection

# from location.models import Location

#
# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = "__all__"

class AdListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ["id", "name", "price", "author"]



class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='first_name',
        read_only=True,
    )

    class Meta:
        model = Ad
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]

class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"

class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"

