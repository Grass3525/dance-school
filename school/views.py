from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from school.models import Classroom, Course, DayOfTheWeek

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
