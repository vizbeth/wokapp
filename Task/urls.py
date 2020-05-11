from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist_view, name='todo'),
    path('edit/<task_id>', views.edit_view, name='edit'),
    path('delete/<task_id>', views.delete_view, name='delete'),
    path('pending/<task_id>', views.pending_view, name='pending'),
    path('done/<task_id>', views.done_view, name='done')
]