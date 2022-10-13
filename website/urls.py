from django.urls import path
from website import views

urlpatterns = [
    path('',views.Home),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
]
