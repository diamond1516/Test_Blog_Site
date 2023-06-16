from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path('about/', views.about),
    path('blog/', views.PostListView.as_view())
]
