from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    pre_requisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_fee_defaulter = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student} enrolled in {self.course}'
