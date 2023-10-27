from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class IndexView(generic.View):
    def get(self, request):
        return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
