from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *









def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username = data['username'],
                password = data['password']
            )
        else:
            return redirect('registration')
        return redirect('login')
    return render(request, 'registration.html')




def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate (
            request,
            username = data['username'],
            password = data['password']
        )
        if user is not None:
            login(request, user)
        return redirect('registration')
    return render(request, 'login.html')



@login_required

def logout_user(request):
    logout(request)
    return redirect('login')



def create_stadium(request):
    if request.method == 'POST':
        Stadium.objects.create(
            caption = request.POST['caption'],
            location = request.POST['location'],
            category_id = request.POST['category'],
            price = request.POST['price'],
            image = request.FILES['image']
        )
        return redirect('show_stadiums')


    categories = Category.objects.all()
    return render(request, 'create_stadium.html', {'categories': categories})




def show_stadiums(request):
    stad = Stadium.objects.all()
    return render(request, 'home.html', {'stad':stad})







@login_required
def stadium_info(request, pk):
    stadium = get_object_or_404(Stadium, id=pk)


    return render(request, 'stadium_info.html', {'stadium': stadium})







@login_required
def my_stadium(request):
    book = request.user.my_booked_stadium_set.all()
    return render(request, 'my_stadium.html', {'book': book})

