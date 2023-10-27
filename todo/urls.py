from django.urls import path

from todo.views import (
    TaskListView,
    IndexView,
    TagListView
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
