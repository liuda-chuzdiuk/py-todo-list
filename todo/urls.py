from django.urls import path
from .views import (
    TaskListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,

)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"
         ),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"
         ),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"
         ),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"
         ),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"
         ),

]

app_name = "todo"
