from django.urls import path
from task_manager.users.views import (
    IndexView,
    UserUpdate,
    UserDelete
)

urlpatterns = [
    path('', IndexView.as_view(), name='users_index'),
    path('<int:id>/update', UserUpdate.as_view(), name='user_update'),
    path('<int:id>/delete', UserDelete.as_view(), name='user_delete'),
]