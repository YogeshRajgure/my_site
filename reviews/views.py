from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

"""class ReviewView(View):
    
    def get(self, request):
        
        form = ReviewForm()
        return render(request, "reviews/index.html", {
            "form": form
        })

    def post(self, request):
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("thank-you")
        
        return render(request, "reviews/index.html", {
            "form": form
        })"""
"""class ReviewView(FormView):

    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "thank-you"

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)"""

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

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     Review_id = kwargs["user_name"]
    #     selected_review = Review.objects.get(pk=Review_id)
    #     context["review"] = selected_review
    #     return context