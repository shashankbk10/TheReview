from django.urls import path
from . import views
from .views import (
            ReviewListView,
            ReviewDetailView,
            ReviewCreateView,
            ReviewUpdateView,
            ReviewDeleteView,
            UserReviewListView,
            )

urlpatterns = [
    path('', ReviewListView.as_view(), name='book-home'),
    path('about/', views.about, name='book-about'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('user/<str:username>/', UserReviewListView.as_view(), name='user-reviews'),
]