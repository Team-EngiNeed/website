from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user with hashed password
            
            # Automatically log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Role-based redirection logic after successful login
                user_role = user.username.upper()  # For case-insensitive matching
                if 'ENGINEED-ADMIN' in user_role or 'PRESIDENT' in user_role:
                    return redirect('engineed:index_new')
                elif 'ENGINEER' in user_role:
                    return redirect('engineed:engineer')
                elif 'ADVISER' in user_role:
                    return redirect('engineed:adviser')
                else:
                    return redirect('engineed:index')  # Default redirect
            else:
                return render(request, 'users/register.html', {'form': form, 'error': 'Authentication failed.'})
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                
                # Role-based redirection logic
                user_role = user.username.upper()  # For case-insensitive matching
                if 'ENGINEED-ADMIN' in user_role or 'PRESIDENT' in user_role:
                    return redirect('engineed:index_new')
                elif 'ENGINEER' in user_role:
                    return redirect('engineed:engineer')
                elif 'ADVISER' in user_role:
                    return redirect('engineed:adviser')
                else:
                    return redirect('engineed:index')  # Default redirect
            else:
                # If user is None (authentication failed), return the form with the error message
                return render(request, 'users/login.html', {'form': form, 'error': 'Incorrect username or password.'})
        else:
            # If the form is not valid, simply return the form with the errors
            return render(request, 'users/login.html', {'form': form})

    else:
        # Initialize a blank form for GET requests
        form = AuthenticationForm()

    # Render the form without errors
    return render(request, 'users/login.html', {'form': form})


# Custom logout view (POST request to logout)
from django.contrib.auth import logout


def logout_view(request):
    logout(request)  # Logout the user
    return redirect('engineed:index')  # Redirect after logout
