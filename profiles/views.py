from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from pathlib import Path
from django.views.generic.edit import CreateView

from .forms import *
from .models import *

# Create your views here.

def store_file(file):
    path =  Path(__file__).resolve().parent / "static" / "profiles" / "images" / str(file["user_image"])
    with open(path, "wb+") as f:
        for chunk in file['user_image'].chunks():
            f.write(chunk)
    print("file saved!")
        


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form =  ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             # store_file(request.FILES)
#             profile = UserProfile(image = request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })