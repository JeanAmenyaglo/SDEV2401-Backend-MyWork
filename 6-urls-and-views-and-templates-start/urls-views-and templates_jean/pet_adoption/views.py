from django.shortcuts import render

# Data for the pets
PET_TYPES = {
    'dog': {
        'name': 'Dog',
        'traits': 'Loyal, energetic, needs space and exercise.',
        'lifestyle_fit': 'active'
    },
    'cat': {
        'name': 'Cat',
        'traits': 'Independent, cuddly, low-maintenance.',
        'lifestyle_fit': 'quiet'
    },
    'rabbit': {
        'name': 'Rabbit',
        'traits': 'Gentle, small, requires calm environment.',
        'lifestyle_fit': 'quiet'
    },
    'parrot': {
        'name': 'Parrot',
        'traits': 'Social, intelligent, needs stimulation.',
        'lifestyle_fit': 'social'
    }
}

# Home page view
def home_page(request):
    return render(request, "pet_adoption/home.html", {"pet_types": PET_TYPES})

# Pet details page
def pet_type_details(request, pet_type):
    pet_data = PET_TYPES.get(pet_type)
    context = {
        "pet_type": pet_type,
        "pet_data": pet_data,
    }
    return render(request, "pet_adoption/pet_details.html", context)

# About page
def about_page(request):
    return render(request, "pet_adoption/about_page.html")