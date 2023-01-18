from django.contrib import admin
from .models import PlacementItem, EventItem

# admin.site.register(PlacementItem)
# admin.site.register(EventItem)

# Register your models here.

@admin.register(PlacementItem)
class PlacementAdmin(admin.ModelAdmin):
    model = PlacementItem
    list_display = ('title', 'institution', 'application_deadline')

@admin.register(EventItem)
class EventAdmmin(admin.ModelAdmin):
    model = EventItem
    list_display = ('type', 'location', 'date')

