from django.shortcuts import render, redirect
from .forms import CreateUserForm,LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Record

# Home Page.
def home(request):
    return render(request, 'webapp/index.html')

# Register Page.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)

# Login Page.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usename = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=usename, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {'form':form}
    return render(request, 'webapp/login.html', context=context)

#User logout
def logout(request):
    auth.logout(request)
    return redirect('login')

# Dashboard Page.
@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records':my_records}

    return render(request, 'webapp/dashboard.html', context=context)

# Add Record Page.
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'webapp/create_record.html', context=context)

# Update Record Page.
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'webapp/update_record.html', context=context)

# Delete Record Page.
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect('dashboard')

# View Record Page.
@login_required(login_url='login')
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'webapp/view_record.html', context=context)


