from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/$', views.games, name='games'),
    url(r'^google_maps/', views.google_maps, name='google_maps'),
    url(r'^games/asteroids/$', views.asteroids, name='asteroids'),
    url(r'^games/flappy/$', views.flappy, name='flappy'),
    url(r'^games/pong/$', views.pong, name='pong'),
    url(r'^games/snake/$', views.snake, name='snake'),
    url(r'^games/space_invaders/$', views.space_invaders, name='space_invaders'),
    url(r'^games/tetris/$', views.tetris, name='tetris'),
    url(r'^games/tic_toe/$', views.tic_toe, name='tic_toe'),
]
