from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class MySignUpView(View):
    form_class = UserCreationForm
    template_name = 'accounts/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            u = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1'),
                    is_active=True
            )


            # TODO Display message and redirect to login
            return HttpResponseRedirect('/accounts/login/?next=/')
        return render(request, self.template_name, {'form': form})


def home(request):
    return render(request, "pages/home.html", {})


@login_required
def profile(request):
    # if not request.POST.get('number'):
    profiles = Profile(user=request.user, first_name=request.POST.get('fname', False),
                       last_name=request.POST.get('lname', False), email=request.POST.get('email', False),
                       number=request.POST.get('number', False), gender=request.POST.get('gender', False))

    if not profiles.first_name and not profiles.gender:
        return render(request, 'accounts/profile.html', {})
    else:
        profiles.save()
        return render(request, 'accounts/showprofile.html', {})


@login_required
def showprofile(request):
        return render(request, 'accounts/showprofile.html', {"user": request.user})
