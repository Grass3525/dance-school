from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from school.models import Classroom, Course, DayOfTheWeek
from schoolmanagement.models import School

__all__ = [
    "ClassroomDetailView",
    "ClassroomListView",
    "CourseCreateView",
    "CourseDeleteView",
    "CourseDetailView",
    "CourseListView",
    "CourseUpdateView",
    "DayOfTheWeekCreateView",
    "DayOfTheWeekDetailView",
    "DayOfTheWeekListView",
    "DayOfTheWeekUpdateView",
    "TimetableView",
]


class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek


class DayOfTheWeekCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = "school.add_dayoftheweek"
    model = DayOfTheWeek
    fields = ["name", "number"]
    success_url = reverse_lazy("dayoftheweek_list")


class DayOfTheWeekUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "school.change_dayoftheweek"
    model = DayOfTheWeek
    fields = ["name", "number"]

    def get_success_url(self):
        return reverse_lazy("dayoftheweek_detail", kwargs={"pk": self.object.pk})


class ClassroomListView(generic.ListView):
    model = Classroom


class ClassroomDetailView(generic.DetailView):
    model = Classroom


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course


class CourseCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = "school.add_course"
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = "school.change_course"
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]

    def get_success_url(self):
        return reverse_lazy("course_detail", kwargs={"pk": self.object.pk})


class CourseDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = "school.delete_course"
    model = Course
    success_url = reverse_lazy("course_list")


class TimetableView(generic.TemplateView):
    """Orario settimanale: righe = orari di inizio, colonne = giorni."""

    template_name = "school/timetable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        school_id = self.request.GET.get("school", "")
        school_id = int(school_id) if school_id.isdigit() else None

        courses = Course.objects.select_related("day_of_the_week", "classroom", "school")
        if school_id:
            courses = courses.filter(school_id=school_id)
        courses = list(courses.order_by("subject"))

        days = list(DayOfTheWeek.objects.order_by("number"))
        hours = sorted({course.starting_hour for course in courses})

        grid = {}
        for course in courses:
            key = (course.starting_hour, course.day_of_the_week_id)
            grid.setdefault(key, []).append(course)

        context["days"] = days
        context["rows"] = [
            {"hour": hour, "cells": [grid.get((hour, day.id), []) for day in days]}
            for hour in hours
        ]
        context["schools"] = School.objects.order_by("name")
        context["selected_school"] = school_id
        return context
