from django.contrib import admin
from .models import user_data,event_info
class userdata_admin(admin.ModelAdmin):
    search_fields=('name','mobile','email',)
    list_display=('name','mobile','email','reg_type','Event','ticket_count')
    list_filter=('reg_type','Event')

class event_admin(admin.ModelAdmin):
    search_fields=('Event_name','Location','Event_date','Event_type')
    list_display=('Event_name','Location','Event_date','Event_type')
    list_filter=('Location','Event_type')
    
    
admin.site.register(user_data,userdata_admin)
admin.site.register(event_info,event_admin)
admin.site.site_header = 'Affairal Admin'

# Register your models here.
