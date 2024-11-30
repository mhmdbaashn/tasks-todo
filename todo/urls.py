from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('todo_list/', views.todo_list, name='todo_list'),
]
