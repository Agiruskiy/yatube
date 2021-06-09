from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='index'),
    path('group/<slug>', views.group_posts, name='groups'),
    #Новый пост
    path('new', views.new_post, name='new_post'),
    path('new/confirm', views.new_post_confirm, name='new_post_confirm'),
    # # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # # Просмотр записи
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    path(
        '<str:username>/<int:post_id>/edit/',
        views.post_edit,
        name='post_edit'
        ),
    path('<str:username>/<int:post_id>/edit_confirm', views.edit_confirm, name='edit_confirm')
    ]