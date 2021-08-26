from django.contrib import admin
# Register your models here.


from .models import *

admin.site.register(Feedbacks)
admin.site.register(Classes)
admin.site.register(Upcoming_Classes)
