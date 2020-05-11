from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages



def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'new account created!')
            return redirect('login')
    return render(request, 'register.html', {'form':form})
