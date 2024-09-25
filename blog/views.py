from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post
from .forms import CommentForm


# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date", ]
    context_object_name = "posts"

    def get_queryset(self):
        query_set =  super().get_queryset()
        data = query_set[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date", ]
    context_object_name = "all_posts"


class SinglePostDetailView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-timestamp"),
            "is_saved_for_later": self.is_stored_post(request, post.slug)
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment_form.save(commit=False)
            comment_form.instance.post = post
            comment_form.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-timestamp"),
            "is_saved_for_later": self.is_stored_post(request, post.slug)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["stored_posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(slug__in = stored_posts)
            context["stored_posts"] = posts 
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        post_id = request.POST["post_id"]

        if stored_posts is None:
            stored_posts = []
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            # request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect(reverse("blog-start-page"))
    

# def starting_page(request):
#     # sorted_posts = sorted(all_posts, key=lambda x:x['date'])
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts":all_posts
#     })

# def post_detail(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html",{
#         "post":identified_post,
#         "post_tags":identified_post.tags.all()
#     })