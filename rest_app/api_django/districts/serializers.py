from rest_framework import serializers
from districts.models import *


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'Name', 'DateCreated', 'Campuses')

    def create(self, validated_data):
        return District.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('Name', instance.Name)
        instance.code = validated_data.get('DateCreated', instance.DateCreated)
        instance.save()
        return instance


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ('id', 'Name', 'DistrictId', 'DateCreated')

    def create(self, validated_data):
        return Campus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('Name', instance.Name)
        instance.code = validated_data.get('DistrictId', instance.DistrictId)
        instance.code = validated_data.get('DateCreated', instance.DateCreated)
        instance.save()
        return instance
