from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from cinema.forms import TicketForm
from cinema.models import Movies,ComingSoonMovie, Ticket
from django.contrib import messages
from account.models import Profile




def index(request):
    movies = Movies.objects.all()
    gelecek_filmler = ComingSoonMovie.objects.all()
    return render(request, 'index.html', {'movies': movies,'gelecek_filmler':gelecek_filmler})


def create_ticket(request):
    if request.method == 'POST':
        # POST isteği gönderildiğinde, kullanıcının verilerini al
        form = TicketForm(request.POST)
        if form.is_valid():
            # Form doğrulandıysa, yeni bir bilet oluştur ve veritabanına kaydet
            movie = form.cleaned_data['movie']
            showtime = form.cleaned_data['showtime']
            price = form.cleaned_data['price']
            new_ticket = Ticket(movie=movie, showtime=showtime, price=price)
            new_ticket.save()
            return redirect('ticket_list')  # Bilet oluşturulduktan sonra kullanıcıyı başka bir sayfaya yönlendir
    else:
        form = TicketForm()  # POST isteği yoksa, boş bir form oluştur

    return render(request, 'create_ticket.html', {'form': form})

def movie_detail(request, slug):
    movie = get_object_or_404(Movies, slug=slug)
    return render(request, 'movie_details.html', {'movie': movie})





def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'index.html', {'movies': movies})

def buy_ticket(request, slug):
    movie = Movies.objects.get(slug=slug)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # Bilet oluştur
            ticket = form.save(commit=False)
            ticket.movie = movie
            ticket.user = request.user
            ticket.save()

            # Kullanıcının profiline bilet ekleyin
            profile = Profile.objects.get(user=request.user)
            profile.tickets.add(ticket)

            messages.success(request, 'Bilet başarıyla satın alındı!')

            # Satın alma işlemi tamamlandıktan sonra film detay sayfasına yönlendir
            return redirect('movie_detail', slug=slug)
    else:
        form = TicketForm()

    return render(request, 'buy_ticket.html', {'form': form, 'movie': movie})


