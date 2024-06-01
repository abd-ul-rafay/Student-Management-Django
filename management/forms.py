from django import forms
from .models import Student, Course, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'age']
        labels = {
            'student_id': 'Student ID',
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'name', 'pre_requisites']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
