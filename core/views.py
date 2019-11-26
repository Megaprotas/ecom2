from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Destination
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Destination
    template_name = 'index.html'
    paginate_by = 6
    queryset = Destination.objects.all()


class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        obj.views += 1
        obj.save()
        return context