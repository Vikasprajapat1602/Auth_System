from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from .forms import CustomUserCreationForm
from .models import Profile




# Home Page
def home(request):
    return render(request, 'home.html')


# Register View

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Create Profile
            profile = Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type'],
                profile_picture=form.cleaned_data['profile_picture'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )
            login(request, user)
            # Redirect to dashboard based on user_type
            if profile.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

    


# Login View
def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully.")
    return redirect('home')


# Dashboard (protected)
@login_required
def dashboard_view(request):
    if request.user.profile.user_type == 'patient':
        return redirect('patient_dashboard')
    else:
        return redirect('doctor_dashboard')


@login_required
def patient_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/patient_dashboard.html', {'profile': profile})

@login_required
def doctor_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/doctor_dashboard.html', {'profile': profile})
