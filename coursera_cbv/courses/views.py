from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Course
from .forms import CourseForm, ColorForm, ColorFormSet


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/course-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['enrolled'] = self.is_student_enrolled(user)
        context['teaching'] = self.is_course_teacher(user)
        return context

    def is_student_enrolled(self, user):
        is_enrolled = False
        is_student = user.is_active and user.is_student
        if is_student:
            is_enrolled = user.student.is_enrolled(self.object.id)
        return is_enrolled

    def is_course_teacher(self, user):
        is_teaching = False
        is_teacher = user.is_active and user.is_teacher
        if is_teacher:
            is_teaching = user.teacher.is_course_teacher(self.object.id)
        return is_teaching


def enroll(request, pk):
    course = Course.objects.get(pk=pk)
    request.user.student.courses.add(course)
    return render(request, 'courses/enroll.html', {'course': course})


def leave(request, pk):
    course = Course.objects.get(pk=pk)
    request.user.student.courses.remove(course)
    return render(request, 'courses/leave.html', {'course': course})


class MyCourseListView(ListView):
    model = Course
    context_object_name = 'my_courses'
    template_name = 'courses/my-courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user.student
        my_courses = student.courses.all()
        context.update({'student': student, 'my_courses': my_courses})
        return context


class MyLecturingView(ListView):
    model = Course
    context_object_name = 'lecturing_courses'
    template_name = 'courses/lecturing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user.teacher
        my_courses = teacher.courses.all()
        context.update({'teacher': teacher, 'my_courses': my_courses})
        return context


def create_course(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('courses:course-list'))
    return render(request, 'courses/create-course.html', {'form': form})


def create_course_formset(request):
    if request.method == "POST":
        formset = ColorFormSet(request.POST)
        for form in formset.forms:
            print(f"You've picked {form.cleaned_data['color']}")
    else:
        formset = ColorFormSet()
    return render(request, 'courses/test_formset.html', {'formset': formset})





class EditCourseView(ListView):
    model = Course
    template_name = 'courses/edit.html'


class LecturingCourseDetailView(DetailView):
    model = Course
    template_name = 'courses/'