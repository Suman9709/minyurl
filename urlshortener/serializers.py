from rest_framework import serializers
from .models import Link

class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields=[
            "original_url"
        ]
    def create(self, validated_data):
        validated_data["owner"]=self.context.get("request").user
        return super().create(validated_data)
    
    
class LinkSerializer(serializers.ModelSerializer):
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