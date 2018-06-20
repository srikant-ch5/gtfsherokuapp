from rest_framework import serializers
from gs.models import GTFSForm
from multigtfs.models import Stop, Agency, Route, Feed
from osmapp.models import Node, Way, KeyValueString, OSM_Relation, Tag


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GTFSForm
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class WaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Way
        fields = '__all__'


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSM_Relation
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class KeyValueStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValueString
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'
