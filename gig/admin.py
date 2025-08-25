from django.contrib import admin

# Register your models here.
from gig.models import *
admin.site.register(User)
admin.site.register(FreelancerProfile)
admin.site.register(ClientProfile)
admin.site.register(UserOnboardingStatus)
