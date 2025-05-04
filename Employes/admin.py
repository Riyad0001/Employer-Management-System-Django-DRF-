from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employer

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person_name', 'email', 'phone_number', 'created_at']
    search_fields = ['company_name', 'contact_person_name']
    list_filter = ['created_at']
