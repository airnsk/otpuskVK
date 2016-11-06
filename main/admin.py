from django.contrib import admin

# Register your models here.
from main.models import zapros

class ZaprosAdmin(admin.ModelAdmin):


    list_display = ('muser_id', 'datezapros','zarp_jan',)
    search_fields = ('muser_id','datezapros', 'zarp_jan',)
    ordering = ('datezapros',)





admin.site.register(zapros,ZaprosAdmin)
