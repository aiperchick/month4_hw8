from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ManListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="man's clothes")

    template_name = "man_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="man's clothes")


class WomenListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="women's clothes")

    template_name = "women_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="women's clothes")


class BabyListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="baby's clothes")

    template_name = "baby_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="baby's clothes")


class SportsWearListView(ListView):
    queryset = models.ProductCl.objects.filter(tags__name="sportswear")

    template_name = "sportswear_list.html"

    def get_queryset(self):
        return models.ProductCl.objects.filter(tags__name="sportswear")


class ClothesDetailView(DetailView):
    template_name = "clothes_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCl, id=product_id)


class OrderClCreateView(CreateView):
    template_name = "add-order.html"
    form_class = forms.OrderClForm
    success_url = "/clothes/"
    queryset = models.OrderCl.objects.all()

    def form_valid(self, form):
        return super(OrderClCreateView, self).form_valid(form=form)
