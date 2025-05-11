from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import User
from myapp.tasks import send_email


def home(request):
    return render(request, "home.html")


def list_users(request):
    users = User.objects.all()
    user_list = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
    return render(request, "users/list.html", {"users": user_list})

def register_user(request):
    # Note: simplified example, use a form to validate input
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not username or not password or not email:
            return JsonResponse({"error": "Missing fields"}, status=400)
        user = User.objects.create(username=username, password=password, email=email)
        send_email.delay(user.pk)
        return JsonResponse({"status": "email queued"})
    else:
        form = {
            "username": "",
            "password": "",
            "email": ""
        }

        return render(request, "registration/register.html", {"form": form})
