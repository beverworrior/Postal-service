from django.shortcuts import render, get_object_or_404, redirect
from .models import Parcel
from .forms import ParcelForm

# Create your views here.
def home(request):
    parcels = Parcel.objects.all()
    return render(request, 'postal/home.html', {'parcels': parcels})

def add_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParcelForm()
    return render(request, 'postal/add_parcel.html', {'form': form})

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

def delete_parcel(request, pk):
    parcel = get_object_or_404(Parcel, pk=pk)
    if request.method == 'POST':
        parcel.delete()
        return redirect('home')
    return render(request, 'postal/delete_parcel.html', {'parcel': parcel})
