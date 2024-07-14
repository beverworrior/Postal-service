from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Parcel
from .forms import ParcelForm, RegisterForm, LoginForm

# Create your views here.
def home(request):
    parcels = Parcel.objects.all()
    return render(request, 'postal/home.html', {'parcels': parcels})

@login_required
def add_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParcelForm()
    return render(request, 'postal/add_parcel.html', {'form': form})

@login_required
def edit_parcel(request, pk):
    parcel = get_object_or_404(Parcel, pk=pk)
    if request.method == 'POST':
        form = ParcelForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParcelForm(instance=parcel)
    return render(request, 'postal/edit_parcel.html', {'form': form})

@login_required
def delete_parcel(request, pk):
    parcel = get_object_or_404(Parcel, pk=pk)
    if request.method == 'POST':
        parcel.delete()
        return redirect('home')
    return render(request, 'postal/delete_parcel.html', {'parcel': parcel})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'postal/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'postal/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')