from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class RoadMapPageView(TemplateView):
    template_name = 'pages/Roadmap.html'


class ActivityPageView(TemplateView):
    template_name = 'pages/activity.html'


class TeamPageView(TemplateView):
    template_name = 'pages/team.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


