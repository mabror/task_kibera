from django.urls import path
from .views import (PostListView, 
                    PostCreateView, 
                    PostUpdateDelete)


urlpatterns = [
    path('api/', PostListView.as_view()),
    path('api/create/', PostCreateView.as_view()),
    path('api/edit/<int:pk>/', PostUpdateDelete.as_view()),
]