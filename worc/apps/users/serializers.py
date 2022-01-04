from rest_framework import serializers

from worc.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "created_at",
            "updated_at",
            "uuid",
            "name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user
