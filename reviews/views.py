from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'reviews/movie_list.html', {'movies': movies})

# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     reviews = Review.objects.filter(movie=movie)
#     return render(request, 'reviews/movie_detail.html', {'movie': movie, 'reviews': reviews})

# @login_required
# def submit_review(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.movie = movie
#             review.user = request.user
#             review.save()
#             return redirect('movie_detail', movie_id=movie_id)
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/submit_review.html', {'form': form, 'movie': movie})


# def movie_search(request):
#     movies = Movie.objects.all()
#     form = MovieSearchForm(request.GET)

#     if form.is_valid():
#         title = form.cleaned_data.get('title')
#         genre = form.cleaned_data.get('genre')
#         release_year = form.cleaned_data.get('release_year')
#         director = form.cleaned_data.get('director')

#         if title:
#             movies = movies.filter(title__icontains=title)
#         if genre:
#             movies = movies.filter(genre__icontains=genre)
#         if release_year:
#             movies = movies.filter(release_year=release_year)
#         if director:
#             movies = movies.filter(director__icontains=director)

#     return render(request, 'movies/movie_search.html', {'movies': movies, 'form': form})


def search_results(request):
    query = request.GET.get('query')
    results = Movie.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results})

@login_required
def rate_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.movie = movie
            rating.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = RatingForm()
    return render(request, 'rate_movie.html', {'form': form, 'movie': movie})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = RatingForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})

