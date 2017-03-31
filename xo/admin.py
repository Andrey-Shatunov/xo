from django.contrib import admin


from .models import Steps
from .models import Statistics
from .models import Room
admin.site.register(Steps)
admin.site.register(Statistics)
admin.site.register(Room)