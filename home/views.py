from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers, BagSerializers, CommentSerializers
from .models import Student, Comment
from commodity.views import BagView
from .forms import SearchHomeForm, CommentForm
from commodity.models import Bag
from django.http import JsonResponse


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
    bag_Serializers = BagSerializers(list_data, many=True)
    return render(
        request,
        "product.html",
        {"form": form, "list_data": list_data, "bag_Serializers": bag_Serializers},
    )


# def AboutView(request):
#     comments = Comment.objects.using("user_db").all().order_by("-created_at")

#     if request.headers.get("x-requested-with") == "XMLHttpRequest":
#         comments_Serializers = CommentSerializers(comments, many=True)
#         return JsonResponse(comments_Serializers.data, safe=False)

#     form = CommentForm()

#     if request.method == "POST":
    
#         if request.user.is_authenticated:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.user = request.user
#                 comment.save()

#                 comments_Serializers = CommentSerializers(comments, many=True)
#                 return JsonResponse(comments_Serializers.data, safe=False)
                
#                 # return redirect("about")
#         else:
#             return redirect("login")
    
    
#     comments_Serializers = CommentSerializers(comments, many=True)
#     json_data = JSONRenderer().render(comments_Serializers.data)
#     json_data = json_data.decode("utf-8")
#     context = {
#         "comments": comments,
#         "form": form,
#     }
#     return render(request, "about.html", context)

def AboutView(request):
    comments = Comment.objects.using("user_db").all().order_by("-created_at")

    # اگر درخواست AJAX باشد، نظرات را به‌صورت JSON برگردان
    if request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "GET":
        comments_Serializers = CommentSerializers(comments, many=True)
        return JsonResponse(comments_Serializers.data, safe=False)

    # مدیریت درخواست POST برای ارسال نظر
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()

                # فقط نظر جدید را سریالایز و برگردان
                comment_Serializers = CommentSerializers(comment)
                return JsonResponse(comment_Serializers.data, safe=False)
        else:
            return JsonResponse({"error": "User not authenticated"}, status=403)

    # برای درخواست‌های معمولی، صفحه HTML را برگردان
    form = CommentForm()
    context = {
        "comments": comments,
        "form": form,
    }
    return render(request, "about.html", context)

@api_view(["GET"])
def Student_List(request):
    student = Student.objects.all()
    students_serializer = StudentSerializers(student, many=True)
    return Response(students_serializer.data)


@api_view(["GET"])
def Commetn_List(request):
    comment = Comment.objects.using("user_db").all().order_by("-created_at")
    comment_serializer = CommentSerializers(comment, many=True)
    return JsonResponse(comment_serializer.data, safe=False)


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
