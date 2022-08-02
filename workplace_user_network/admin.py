from django.contrib import admin
from workplace_user_network.models import Department, Division, Interaction, User, WorkplaceUserNetwork

# Register your models here.
admin.site.register(WorkplaceUserNetwork)
admin.site.register(User)
admin.site.register(Division)
admin.site.register(Interaction)
admin.site.register(Department)