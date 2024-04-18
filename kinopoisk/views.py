from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kinopoisk/home.html')

def movie_detail(request,movie_id):
    return render(request, 'movies/detail/movie_detail.html')

def composer_detail(request,composer_id):
    return render(request, 'movies/detail/composer_detail.html')

def genre_detail(request,genre_id):
    return render(request, 'movies/detail/genre_detail.html')

def director_detail(request,genre_id):
    return render(request, 'movies/detail/director_detail.html')

def actor_detail(request,actor_id):
    return render(request, 'movies/detail/actor_detail.html')

def actors_list(request):
    return render(request, 'movies/list/actor_list.html')

def composers_list(request):
    return render(request, 'movies/list/composers_list.html')

def directors_list(request):
    return render(request, 'movies/list/directors_list.html')

def gengres_list(request):
    return render(request, 'movies/list/gengres_list.html')

def movies_list(request):
    return render(request, 'kinopoisk/list/movies_list.html')