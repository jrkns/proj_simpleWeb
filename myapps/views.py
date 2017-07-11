from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapps/index.html')
def games(request):
    return render(request, 'myapps/games/index.html')
def google_maps(request):
    return render(request, 'myapps/google_maps/index.html')
def asteroids(request):
    return render(request, 'myapps/games/asteroids/index.html')
def flappy(request):
    return render(request, 'myapps/games/flappy/index.html')
def pong(request):
    return render(request, 'myapps/games/pong/index.html')
def snake(request):
    return render(request, 'myapps/games/snake/index.html')
def space_invaders(request):
    return render(request, 'myapps/games/space_invaders/index.html')
def tetris(request):
    return render(request, 'myapps/games/tetris/index.html')
def tic_toe(request):
    return render(request, 'myapps/games/tic_toe/index.html')
