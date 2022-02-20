from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("loadFile/", views.load_from_file, name="load-from-file"), 
    path("loadFileResult/", views.load_from_file_result, name="load-from-file-result")
]
 