from django.shortcuts import render
from . import models
from django.views import generic

# Create your views here.#


def home(request):
    profile = models.ProfileData.objects.first()
    tools = models.Tool.objects.all().order_by("order")
    social_links = models.SocialLink.objects.all().order_by('order')
    about = models.About.objects.last()
    services = models.Service.objects.all().order_by('order')
    categories = models.Category.objects.all()
    projects = models.Project.objects.all()[:4]
    posts = models.Post.objects.all()[:4]

    context = {
            "profile": profile,  # 1 dona
            "tools": tools,  # query set
            "social_links": social_links,
            "about": about,
            "services": services,
            'categories': categories,
            'projects': projects,
            "posts": posts
               }

    return render(request, 'index.html', context)


def about(request):
    about = models.About.objects.last()
    tools = models.Tool.objects.all()
    context = {
        "about": about,
        "tools": tools
    }
    return render(request, "about-us.html", context)


class PostListView(generic.ListView):
    model = models.Post
    context_object_name = "posts"
    template_name = "blog.html"



def portfolio(request):
    categories = models.Category.objects.all()
    portfolis = models.Project.objects.all()
    context = {
        "projects": portfolis,
        "categories": categories
    }
    return render(request, "portfolio.html", context)