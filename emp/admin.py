from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','emp_id')
    search_fields=('name','phone')
    list_filter=('working',)

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)