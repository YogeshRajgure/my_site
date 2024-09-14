from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="book-store-start-page"),
    path("<slug:slug>", views.book_detail, name="book-details-page")
    
]
