from .models import *
from rest_framework.serializers import ModelSerializer


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = ('phone_number', 'email', 'address', 'description')


class TypeActivitySerializer(ModelSerializer):
    class Meta:
        model = TypeActivity
        fields = ('id', 'name', 'description')


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ('description', 'type_activity_id')


class RepairSerializer(ModelSerializer):
    class Meta:
        model = Repair
        fields = ('photo', 'title', 'description')


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'photo')


class ProjectSerialiazer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('photo', 'title', 'description')

    
class FeedBackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'address', 'message')


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('whatsapp_link', 'instagram_link', 'facebook_link', 'vk_link')