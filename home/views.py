from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import StudentSerializers, BagSerializers
from .models import Student
from commodity.views import BagView
from .forms import SearchHomeForm
from commodity.models import Bag
from django.http import HttpResponse

# Create your views here.


def HomeView(request):

    context = {}
    return render(request, "./home.html", context)


@login_required(login_url="login")
@user_passes_test(lambda x: x.is_authenticated)
def DiscountView(request):
    context = {}
    if request.method == "POST":
        

        if not request.user.is_authenticated:
            return redirect("login")
        

        return render(request, "discount.html", context)
    else:
        return render(request, "discount.html", context)


def DroductView(request):
    form = SearchHomeForm()
    results = []

    if request.method == "POST":
        form = SearchHomeForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Bag.objects.filter(bag_name__icontains=query)
            return render(request, "search.html", {"form": form, "results": results})

    list_data = Bag.objects.all()
    bag_Serializers= BagSerializers(list_data , many=True)
    return render(request, "product.html", {"form": form, "list_data": list_data, 'bag_Serializers' :bag_Serializers })


def AboutView(request):
    context = {}
    return render(request, "about.html", context)


@api_view(["GET"])
def Student_List(request):
    student = Student.objects.all()
    students_serializer = StudentSerializers(student, many=True)
    return Response(students_serializer.data)


@api_view(["GET"])
def Student_Details(request, pk):
    student = Student.objects.get(id=pk)
    student_serializer = StudentSerializers(student, many=False)
    return Response(student_serializer.data)


@api_view(["POST"])
def Student_save(request):
    student = StudentSerializers(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data)


@api_view(["POST"])
def Student_update(request, pk):
    instance = Student.objects.get(id=pk)
    student = StudentSerializers(instance=instance, data=request.data)
    if student.is_valid():
        student.save()
        pass
    return Response(student.data)


@api_view(["DELETE"])
def Student_delete(request, pk):
    instance = Student.objects.get(id=pk)
    instance.delete()

    return Response("student deleted!")
