from django.shortcuts import render, redirect
from .models import Student, Video
from .forms import StudentLoginForm


def index(request):
    return render(request, "index.html")


def student_login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            grade = form.cleaned_data["grade"]

            # Check if student exists, or create a new one
            student, created = Student.objects.get_or_create(name=name, grade=grade)

            # Store student info in session
            request.session["student_id"] = student.id
            request.session["student_name"] = student.name
            request.session["grade"] = student.grade
            request.session["grade_display"] = student.get_grade_display_name()

            return redirect("videos")
    else:
        form = StudentLoginForm()

    return render(request, "login.html", {"form": form})


def videos(request):
    # Check if student is logged in
    if "student_id" not in request.session:
        return redirect("login")

    student_name = request.session.get("student_name")
    grade = request.session.get("grade")
    grade_display = request.session.get("grade_display")

    # Get videos for the student's grade
    videos = Video.objects.all()
    # videos = Video.objects.filter(grade=grade)

    context = {
        "student_name": student_name,
        "grade": grade,
        "grade_display": grade_display,
        "videos": videos,
    }

    return render(request, "videos.html", context)


def logout(request):
    # Clear session data
    request.session.flush()
    return redirect("index")
