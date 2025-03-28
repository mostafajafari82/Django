from django.urls import path
from .views import *
from django.views.generic import TemplateView
from commodity.views import SearchView

urlpatterns = [
    path('home', HomeView, name='home'),
    path('product/', DroductView, name='product'),
    path('homesearch/', HomeView, name='homesearch'),
    path('discount/', DiscountView, name='discount'),
    path('about/', AboutView, name='about'),


    # path("search", SearchView, name='search'),
    path("comment_list", Commetn_List),
    # path("student_details/<pk>", Student_Details),
    # path("student_save", Student_save),
    # path("student_update/<pk>", Student_update),
    # path("student_delete/<pk>", Student_delete),
]