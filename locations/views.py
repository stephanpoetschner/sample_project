from django.shortcuts import render, redirect
from .forms import LocationForm, LocationImageForm
from .models import Location


def home(request):
    locations = Location.objects.all()
    return render(request, 'locations/home.html', {'locations': locations})


def add_location(request):
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        image_form = LocationImageForm(request.POST, request.FILES)

        if location_form.is_valid() and image_form.is_valid():
            location = location_form.save()
            image = image_form.save(commit=False)
            image.location = location
            image.save()
            return redirect('home')
    else:
        location_form = LocationForm()
        image_form = LocationImageForm()

    return render(request, 'locations/add_location.html', {'location_form': location_form, 'image_form': image_form})
