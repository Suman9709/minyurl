
from rest_framework import serializers
from .models import Link
from urlshortener.utils import convert_to_base_62
from core.serializers import UserSerializer

class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields=[
            "original_url"
        ]
    def create(self, validated_data):
        # request = self.context["request"]
        # validated_data["owner"] = request.user
        
        # we can use both
        validated_data["owner"]=self.context.get("request").user
        instance = Link.objects.create(**validated_data)
        short_code = convert_to_base_62(instance.id)
        instance.short_code = short_code
        instance.save()
        return instance
        
    
    
class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)
    original_url = serializers.CharField(read_only=True)
    short_code = serializers.CharField(read_only=True)
    clicks_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Link
        fields=[
            "id",
            "original_url",
            "short_code",
            "clicks_count",
            "expires_at",
            "is_Active",
            "created_at"
        ]