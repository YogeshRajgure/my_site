from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(), name="reviews-start-page"),
    path("thank-you", views.ThankyouView.as_view(), name="thank-you-page"),
    path("reviews-list", views.ReviewListView.as_view(), name="reviews-list-page"),
    path("reviews-list/favourite", views.AddFavouriteView.as_view(), name="mark-review-as-fav"),
    path("reviews-list/<str:pk>", views.ReviewDetailView.as_view(), name="reviews-details-page")
]
