from django.urls import path

from todo.views import (
    TaskListView,
    IndexView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"
