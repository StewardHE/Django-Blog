from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

from posts.models import Post

# view for create the user
User = get_user_model()

def user_create_view(request):
    if request.method == "POST":
        context = {}
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
           # Create user
           username = request.POST['username']
           email = request.POST['email']

        # Check if the user already exists
           try:
                # if the user already exists, finds the user and email in the database 
               user1 = User.objects.get(username = username)
               context['error'] = "Username or email is already in the system!"
               return render(request, 'accounts/create.html', context = context)
           except User.DoesNotExist:
                try:
                  user2 = User.objects.get(email = email)
                   # sends a message
                  context['error'] = "Username or email is already in system!"
                  return render(request, 'accounts/create.html', context = context) 
        # If the user not exist in database 
                except User.DoesNotExist:
                    # Create the user
                        user = User.objects.create_user(username = username, email = email, password = password1)
                        return redirect('posts:list')      
        else:
            context['error'] = "Passwords must match!"
            return render(request, 'accounts/create.html', context = context)
    else:
        return render(request, 'accounts/create.html')

# view for user login
def user_login_view(request):
    if request.method == "POST":
         context = {}
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username = username, password = password)
        # check if the user exists in database
         if user is not None:
             login(request, user) # login the user
             context['success'] = "You are logged in!" # send a message 
             return render(request, 'accounts/login.html', context)
        # if the user not exist in database
         else:
            context['error'] = "Invalid Login"
            return render(request, 'accounts/login.html', context)
    else:   
        return render(request, 'accounts/login.html')

# view for logout 
def user_logout_view(request):
    if request.user.is_authenticated:
        # log out user
        logout(request)
        return render(request, 'accounts/logout.html')
    else:
        return redirect('accounts:login')

# view for user profile 
def user_profile_view(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author = user)
    context = {'posts':posts}
    return render(request, 'accounts/profile.html', context = context)

