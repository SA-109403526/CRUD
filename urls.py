from django.urls import path
from .import views

 
urlpatterns = [
    path('hello/',  views.say_hello),
    path('',views.home,name = 'home'),
    # 跑進project
    path('project/<str:pk>/',views.projects,name="project"),
    path('create-project/',views.createproject,name ="create-project"),
    path('update-project/<str:pk>/',views.updateproject,name ="update-project"),
    path('delete-project/<str:pk>/',views.deleteproject,name ="delete-project"),
]
