from django.shortcuts import render, redirect
from .forms import HealthCheckForm
from django.urls import reverse

def is_healthy(age, weight):
    # Simple example of healthy weight ranges by age group
    healthy_weight_ranges = {
        (0, 1): (3.5, 12),  # Infants
        (2, 4): (10, 18),  # Toddlers
        (5, 8): (17, 26),  # Children
        (9, 12): (25, 40),  # underteens
        (13, 18): (39, 98),  # Teenagers
        (19, 40): (50, 100),  # Adults
        (41, 60): (50, 100),  # Middle-aged
        (61, 100): (45, 85),  # Seniors
    }
    
    # Find the age range that includes the user's age
    for age_range, weight_range in healthy_weight_ranges.items():
        if age_range[0] <= age <= age_range[1]:
            return weight_range[0] <= weight <= weight_range[1]

    # If age is outside defined ranges, return False
    return False

# def health_check_view(request):
#     if request.method == 'POST':
#         form = HealthCheckForm(request.POST)
#         if form.is_valid():
#             age = form.cleaned_data['age']
#             weight = form.cleaned_data['weight']

#             result = "healthy" if is_healthy(age, weight) else "not healthy"

#             return render(request, 'hms/check_result.html', {'result': result})
    
#     # Redirect to the form page to avoid carrying over data
#     return redirect(reverse('health_check'))  # 'health_check' is the name of the form view


def health_check_view(request):
    if request.method == 'POST':
        form = HealthCheckForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            if is_healthy(age, weight):
                result = "healthy"
            else:
                result = "not healthy"
            return render(request, 'hms/check_result.html', {'result': result})
    else:
        form = HealthCheckForm()
    
    return render(request, 'hms/check_form.html', {'form': form})