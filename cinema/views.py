from django.shortcuts import render, get_object_or_404
from cinema.models import Movies,ComingSoonMovie


def index(request):
    context = {
        "cinemas":Movies.objects.all(),
        "gelecek_filmler":ComingSoonMovie.objects.all()
    }
    return render(request,"pages/index.html",context)

# def movie_details(request,slug):
#     movie=Movie.objects.get(slug=slug)
#     return render(request,"page/movie-details.html", {
#         "slug":movie
#     })


# def movie_details(request, slug):
#     slug = get_object_or_404(Movies, slug=slug)
#     # movie = Movies.objects.get(slug=slug)
#     return render(request, 'pages/movie-details.html', {
#             'slug': slug
#         }
#     )

def movie_details(request, slug):
    movie = Movies.objects.get(slug=slug)
    return render(request, 'movie_details.html', {'movie': movie})




def movie_details(request, slug):
    movie = get_object_or_404(Movies, slug=slug)
    return render(request, 'pages/movie_details.html', {
        'movie': movie
    })