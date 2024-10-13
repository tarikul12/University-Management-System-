from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import UserProfileForm


# Define a view function for the login page
def user_login(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('login')
        else:
            # Log in the user and redirect to the home page upon successful login
            auth_login(request, user)
            return redirect('dashboard')
    
    # Render the login page template (GET request)
    return render(request, 'account/login.html')

# Define a view function for the registration page
def register(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('register')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('register')
    
    # Render the registration page template (GET request)
    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out.")
    return redirect("login")



def dashboard(request):
    return render(request, 'account/dashboard.html')



def edit_profile(request):
    if request.method == 'POST':
        # Pass the user's current data to the form for validation
        form = UserProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            # Save the updated user profile
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('edit_profile')
    else:
        # Pre-populate the form with the current user's data
        form = UserProfileForm(instance=request.user)

    # Render the edit profile template with the form
    return render(request, 'account/edit_profile.html', {'form': form})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Keep the user logged in after changing the password
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'account/change_password.html', {'form': form})
