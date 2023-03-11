from django.contrib import admin
from .models import (Investor, BusinessOwner, 
                    Business, BlockedUser)

admin.site.register(Business)
admin.site.register(BusinessOwner)
admin.site.register(Investor)
admin.site.register(BlockedUser)