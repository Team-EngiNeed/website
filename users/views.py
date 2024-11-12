from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # 'username' here represents the email
            password = form.cleaned_data['password']
            UserModel = get_user_model()
            
            try:
                # Case-insensitive lookup for email
                user = UserModel.objects.get(username__iexact=username)  # Email should be unique
                if user.check_password(password):  # Check if the password is correct
                    login(request, user)  # Log the user in

                    # Redirect based on username content
                    username = user.username.upper()  # Optional: Make it case-insensitive for role check
                    if 'ENGINEED-ADMIN' in username:
                        return redirect('engineed:index_new')
                    elif 'PRESIDENT' in username:
                        return redirect('engineed:index_new')
                    elif 'ENGINEER' in username:
                        return redirect('engineed:engineer')
                    elif 'ADVISER' in username:
                        return redirect('engineed:adviser')
                    else:
                        # Default redirect if no keyword is found
                        return redirect('engineed:index')

            except UserModel.DoesNotExist:
                form.add_error('username', 'User with this email does not exist.')
        else:
            form.add_error(None, 'Incorrect email or password.')  # General error for other cases

    else:
        form = AuthenticationForm()  # Display an empty form if GET request

    return render(request, 'users/login.html', {'form': form})

# Custom logout view (POST request to logout)
from django.contrib.auth import logout


def logout_view(request):
    logout(request)  # Logout the user
    return redirect('engineed:index')  # Redirect after logout
