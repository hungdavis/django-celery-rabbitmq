from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 10
    ordering = ('id',)
