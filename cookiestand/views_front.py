from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookiestand/cookiestand_list.html"
    model = CookieStand
    context_object_name = "cookiestand"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookiestand/cookiestand_detail.html"
    model = CookieStand


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookiestand/cookiestand_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookiestand/cookiestand_create.html"
    model = CookieStand
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookiestand/cookiestand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookiestand_list")
