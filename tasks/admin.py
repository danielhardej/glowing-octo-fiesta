from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin interface for Task model"""

    list_display = [
        "title",
        "status",
        "priority",
        "assigned_to",
        "created_at",
        "due_date",
    ]
    list_filter = ["status", "priority", "created_at", "assigned_to"]
    search_fields = ["title", "description"]
    list_editable = ["status", "priority"]
    date_hierarchy = "created_at"
    raw_id_fields = ["assigned_to"]

    fieldsets = (
        (None, {"fields": ("title", "description")}),
        (
            "Status & Priority",
            {"fields": ("status", "priority", "assigned_to"), "classes": ("collapse",)},
        ),
        ("Dates", {"fields": ("due_date",), "classes": ("collapse",)}),
    )

    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        queryset = super().get_queryset(request)
        return queryset.select_related("assigned_to")
