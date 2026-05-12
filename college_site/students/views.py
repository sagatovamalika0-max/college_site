from django.shortcuts import render,redirect
from .models import Student, Group
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect



def student_list(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})



def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            age=request.POST.get("age"),

            # 🔥 ВАЖНО: берем ID группы
            group=Group.objects.get(id=request.POST.get("group")),

            photo=request.FILES.get("photo")
        )
        return redirect("student_list")

    groups = Group.objects.all()
    return render(request, "students/add_student.html", {"groups": groups})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.age = request.POST.get("age")
        student.group = request.POST.get("group")
        student.save()
        return redirect("student_list")

    return render(request, "students/edit_student.html", {"student": student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "students/register.html", {"form": form})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "students/detail.html", {"student": student})