from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Job_Title', 'Biodata']    
admin.site.register(Person, PersonAdmin)