from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Student, Video


def student_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            grade = form.cleaned_data["grade"]
            try:
                student = Student.objects.get(name=name, grade=grade)
                request.session["student_id"] = student.student_id
                return redirect("video_section")
            except Student.DoesNotExist:
                return render(
                    request,
                    "login.html",
                    {"form": form, "error": "Invalid credentials"},
                )
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def video_section(request):
    if "student_id" not in request.session:
        return redirect("student_login")

    try:
        student = Student.objects.get(student_id=request.session["student_id"])
        videos = Video.objects.filter(grade=student.grade)
        return render(request, "videos.html", {"videos": videos})
    except Student.DoesNotExist:
        return redirect("student_login")


def logout_view(request):
    request.session.flush()
    return redirect("student_login")
