from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task_manager.users.views import (
    IndexView,
    UserUpdateView,
    UserDelete,
    UserCreateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='users_index'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:id>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:id>/delete/', UserDelete.as_view(), name='user_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
