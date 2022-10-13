from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index, name="blog-index"),
    path('cat/<int:id>/',views.ReadCat, name="blog-cat"),
    path('readBlog/<int:id>/',views.ReadBlog, name="readblog"),
]
