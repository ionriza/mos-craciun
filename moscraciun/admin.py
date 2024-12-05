from django.contrib import admin
from .models import Wishing, Elf


@admin.register(Wishing)
class WishingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "age",
        "gender",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "gender")
    search_fields = ("name", "wishing_items")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Elf)
class ElfAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",
        "associated_letter",
        "sent",
        "created_at",
        "updated_at",
    )
    list_filter = ("sent",)
    search_fields = ("name", "email", "phone_number", "associated_letter__name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
