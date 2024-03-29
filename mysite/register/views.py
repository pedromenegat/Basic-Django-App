from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Question, Choice

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Your account has been created! You are now able to log in.')
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!.')
            return redirect("/profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)     

    question = Question.objects.all()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'question': question
    }

    return render(request, 'register/profile.html', context)