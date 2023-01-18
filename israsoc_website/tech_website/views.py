from django.shortcuts import render
from .models import PlacementItem, EventItem
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class HomeView(TemplateView):
    template_name="tech_website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = EventItem.objects.all()
        context["placements"] = PlacementItem.objects.all()
        return context

class PlacementsView(ListView):
    model = PlacementItem
    template_name = "tech_website/placements.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = EventItem.objects.all()
        context["placements"] = PlacementItem.objects.all()
        return context
        
class EventsView(ListView):
    model = EventItem
    template_name = "tech_website/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = EventItem.objects.all()
        context["placements"] = PlacementItem.objects.all()
        return context

