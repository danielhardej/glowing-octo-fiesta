from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""

    assigned_to_detail = UserSerializer(source="assigned_to", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "status",
            "assigned_to",
            "assigned_to_detail",
            "created_at",
            "updated_at",
            "due_date",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value):
        """Validate that title is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value
