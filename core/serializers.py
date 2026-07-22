from django.contrib.auth import get_user_model
from rest_framework import serializers

from urlshortener.models import Link



User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = [
            "id",
            "username",
            "email",
            "password"
        ]
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "username",
#             "email",
#             "is_staff",
#             "is_superuser",
#             "is_active",
#             "date_joined",
#         ]

class UserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            "id",
            "original_url",
            "short_code",
            "clicks_count",
            "is_Active",
        ]


class UserSerializer(serializers.ModelSerializer):
    links = UserLinkSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "links",
        ]