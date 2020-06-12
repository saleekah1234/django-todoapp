from django.urls import include,path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.todo_view,name='todo_view'),
    path('addTodo/',views.add_todo,name='add_todo'),
    path('deleteTodo/<int:pk>/',views.delete_todo,name=' delete_todo')
    ]