from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('finished/<int:todo_id>/', views.finished, name='finished'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('edit/<int:todo_id>/update', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete')
]