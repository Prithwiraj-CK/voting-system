from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Custom admin view for our User model"""
    
    model = CustomUser
    
    # What columns to show in the user list
    list_display = [
        'username', 
        'email', 
        'role', 
        'has_voted', 
        'is_staff',
        'created_at'
    ]
    
    # Add filters on the right side
    list_filter = ['role', 'has_voted', 'is_staff']
    
    # Add our custom fields to the admin form
    fieldsets = UserAdmin.fieldsets + (
        ('Voting Info', {
            'fields': ('role', 'date_of_birth', 'has_voted')
        }),
    )
    
    # Fields shown when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Voting Info', {
            'fields': ('role', 'date_of_birth')
        }),
    )


# Register the model with our custom admin
admin.site.register(CustomUser, CustomUserAdmin)

# Customize admin site header
admin.site.site_header = "Voting System Admin"
admin.site.site_title = "Voting System"
admin.site.index_title = "Welcome to Voting System Admin"