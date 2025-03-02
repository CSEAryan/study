# student_portal/urls.py
from django.contrib import admin
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.student_login, name="student_login"),
    path("videos/", views.video_section, name="video_section"),
    path("logout/", views.logout_view, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
