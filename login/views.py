from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def doc_login(request):
    if request.user.is_authenticated:
        return redirect('/patient')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        login(request, user)

        if user != None:
            return redirect('/patient')
        else:
            print('wrong detail')

    return render(request, 'login&registration/doc_login.html')
