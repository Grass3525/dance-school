from django.contrib import admin

from school.models import Classroom, Course, DayOfTheWeek

admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(DayOfTheWeek)
