from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Code
from SMS.models import CustomUser
from .forms import CodeForm
from .utils import send_sms

@login_required
def home_page(request):
    return render(request, 'main.html')


def authentication_view(request):
    form = AuthenticationForm() # this present form with username and password for login
    if request.method == "POST":
        # getting username and password from the user input
        username = request.POST.get('username') 
        password = request.POST.get('password')

        # authenticating user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify')
    return render(request, 'auth.html', {'form':form})

def verification(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f'{user.username}: {user.code}'
        
        if not request.POST: # To avoide code sending twice
            send_sms(code_user, user.phone_number)
        if form.is_valid():
            # getting the number
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('home')
            else:
                return redirect('authenticate')
        return render(request, 'verify.html', {'form':form})
