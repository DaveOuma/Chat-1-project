from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	context = {}
 
	return render(request, "chat/chat_page.html", context)

def login_chat_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # Redirect to chat page after successful login
            return redirect('chat-page')
        else:
            # Display an error message or handle login failure appropriately
            # ...
    # Render the login form with context (if needed)
            return render(request, 'chat/chat_page.html')
