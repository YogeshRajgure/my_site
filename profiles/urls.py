from django.urls import path


from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="profiles-start-page"),
    path("list", views.ProfilesView.as_view(), name="profiles-list-page")
] 
