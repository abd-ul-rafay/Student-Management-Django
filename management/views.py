from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm

def index(request):
    return render(request, 'management/index.html')

class StudentListView(ListView):
    model = Student
    template_name = 'management/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(student_id__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fee_defaulters = Enrollment.objects.filter(is_fee_defaulter=True)
        context['fee_defaulters'] = fee_defaulters
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'management/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'management/student_form.html'
    success_url = reverse_lazy('students')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'management/student_form.html'
    success_url = reverse_lazy('students')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'management/student_confirm_delete.html'
    success_url = reverse_lazy('students')

class CourseListView(ListView):
    model = Course
    template_name = 'management/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(course_code__icontains=query))
        return queryset

class CourseDetailView(DetailView):
    model = Course
    template_name = 'management/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'management/course_form.html'
    success_url = reverse_lazy('courses')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'management/course_form.html'
    success_url = reverse_lazy('courses')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'management/course_confirm_delete.html'
    success_url = reverse_lazy('courses')

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'management/enrollment_form.html'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        student = form.cleaned_data['student']
        course = form.cleaned_data['course']
        pre_reqs = course.pre_requisites.all()
        
        # Check if student is enrolled in all prerequisites
        for pre_req in pre_reqs:
            if not Enrollment.objects.filter(student=student, course=pre_req).exists():
                form.add_error(None, f'Student must be enrolled in prerequisite course: {pre_req.name}')
                return self.form_invalid(form)

        return super().form_valid(form)

def remove_defaulter(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    student_id = enrollment.student.pk
    enrollment.is_fee_defaulter = False
    enrollment.save()

    return redirect('student-detail', pk=student_id)

def fee_defaulter_list(request):
    defaulters = Enrollment.objects.filter(is_fee_defaulter=True).select_related('student', 'course')
    context = {'defaulters': defaulters}
    return render(request, 'management/fee_defaulter_list.html', context)
