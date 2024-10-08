from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    
    model = Review
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "thank-you"
    

class ThankyouView(TemplateView):
    template_name = "reviews/thankyou.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "this works"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    
    
class ReviewDetailView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get("favourite_review")
        context["is_fav_key"] = str(fav_id) == str(loaded_review.user_name)
        return context



class AddFavouriteView(View):
    def post(self, request):
        pk = request.POST["review_id"]
        request.session["favourite_review"] = pk
        return HttpResponseRedirect("/reviews/reviews-list/"+pk) 
        # return reverse("reviews-details-page", args=[pk])