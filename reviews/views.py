from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm

# Create your views here.

class ReviewView(View):
    
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
        })


def thank_you(request):
    return render(request, "reviews/thankyou.html")