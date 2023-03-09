from django.urls import path
from . import views

urlpatterns = [
    path("clothes/", views.ManListView.as_view(), name="man's clothes"),
    path("clothes/", views.WomenListView.as_view(), name="women's clothes"),
    path("clothes/", views.BabyListView.as_view(), name="baby's clothes"),
    path("clothes/", views.SportsWearListView.as_view(), name="sportswear"),
    path("clothes/<int:id>/", views.ClothesDetailView.as_view(), name="detail"),
    path("add-order/", views.OrderClCreateView.as_view(), name="add-order"),
]
