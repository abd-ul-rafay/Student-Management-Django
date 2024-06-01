from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-edit'),
    path('course/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('enrollment/add/', views.EnrollmentCreateView.as_view(), name='enrollment-add'),
    path('enrollment/<int:pk>/remove_defaulter/', views.remove_defaulter, name='remove-defaulter'),
    path('fee_defaulters/', views.fee_defaulter_list, name='fee-defaulter-list'),
]
