from django.urls import path
from . import views

app_name = 'edward_app' 

urlpatterns = [
    path('Home',views.Home.as_view()),
    path('naruto/',views.Naruto.as_view()),
    path('DemonSlayer/',views.Demon.as_view()),
    path('Pokémon/',views.Pokemon.as_view()),
    path('OnePiece/',views.MyHero.as_view()),

]
