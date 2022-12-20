from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm
# Create your views here.

@permission_required('user.is_staff',login_url="../admin")
def login(request):
    
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = LoginForm()
        return render(request, "accounts/login.html", form)