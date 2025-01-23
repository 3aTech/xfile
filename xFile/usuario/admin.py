from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Profile

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# PROFILE DETALLADO
class ProfileResource(resources.ModelResource):
    ''''''
    class Meta:
        model = Profile
        
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =['user', 'address', 'location', 'phone', 'user_group']
    search_fields = ['location', 'user__username', 'user__groups__name']
    list_filter = ['user__groups', 'location']
    
    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = 'Grupo'
    resource_class = ProfileResource
admin.site.register(Profile, ProfileAdmin)