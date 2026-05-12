from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.add_student, name="add_student"),
 path("students/<int:id>/", views.student_detail, name="detail"),
    path("students/<int:id>/edit/", views.edit_student, name="edit_student"),
    path("students/<int:id>/delete/", views.delete_student, name="delete_student"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="students/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
