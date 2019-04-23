from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html', {"title": "About us"})


def contact_page(request):
    return render(request, 'Hello_World.html', {"title": "Contact us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "Hello_World.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)                           #(request, 'Hello_World.html', {"title": "Contact us"})

