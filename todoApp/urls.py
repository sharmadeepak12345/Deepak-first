from django.urls import path
from . import views

urlpatterns=[
    path('markDone/<int:pk>',views.markDone,name='markDone'),
    path('mark_unDone/<int:pk>',views.mark_unDone,name='mark_unDone'),
    path('remove_task/<int:pk>',views.remove_task,name='remove_task'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
    path('addTask/',views.addTask,name='addTask')
]