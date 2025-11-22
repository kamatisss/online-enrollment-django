from django.contrib import admin
from .models import Personal_Background, Education_Background, Family_Background, Course, Tuition

admin.site.register(Personal_Background)
admin.site.register(Education_Background)
admin.site.register(Family_Background)
admin.site.register(Course)
admin.site.register(Tuition)
