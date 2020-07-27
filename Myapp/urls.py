from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('quiz/',views.quiz,name='quiz'),
    path('instructions/',views.instructions,name='instructions'),
    path('contact/',views.contact,name="contact"),
    path('send/',views.send,name="send"),
    path('profile/',views.profile,name="profile")
]