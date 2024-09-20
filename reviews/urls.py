from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(), name="reviews-start-page"),
    path("thank-you", views.thank_you, name="thank-you-page")
]
