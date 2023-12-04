from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User




default_value = timezone.now

class Genres(models.Model):
    ad = models.CharField(max_length=100, unique=True, help_text="Film türünün adı")

    def __str__(self):
        return self.ad
    

class Seanslar(models.Model):
    starttime = models.TimeField()
    endtime = models.TimeField()


    #starttime endtime 2 tane datetime açılacak

    def __str__(self):
        starttime = str(self.starttime)
        endtime = str(self.endtime)
        return f'{starttime} - {endtime}'
    
    def __unicode__(self):
        return f"{self.starttime}-{self.endtime}"



class Salon(models.Model):
    name = models.TextField()# bunun yerine id de kullanılabilir
    is_active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField()
    #2d ve 3d ayır


    def __str__(self):
        return f"{self.name}"



class Movies(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=33)
    director = models.CharField(max_length=20)
    cast = models.TextField(max_length=75)
    twod = models.BooleanField(default=False)  # sadece 3d çıkan film olmaz bunu sonra sil
    threed = models.BooleanField(default=False)
    description = models.TextField(max_length=250)
    slug = models.SlugField(null=False, blank=True, unique=True,db_index=True,editable=False)
    image = models.ImageField(max_length=100)
    #showtimes = models.ManyToManyField('Showtime', related_name='cinema_halls') bir hata
    is_active = models.BooleanField(default=True)
    seans_starttime = models.ManyToManyField(Seanslar, related_name='seanslar')
    #salon_no = models.ForeignKey(Salon, on_delete = models.DO_NOTHING )
    trailer_url = models.URLField(max_length=200)
    release_year = models.IntegerField()
    imbd_rating = models.FloatField()
    image1 = models.ImageField(max_length=100)
    image2 = models.ImageField(max_length=100)
    image3 = models.ImageField(max_length=100)
    turler = models.ManyToManyField(Genres, help_text="Film türleri")
    # film süresi

    def __str__(self):
        return f"{self.title}"

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)



class ComingSoonMovie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    description = models.TextField()
    trailer_url = models.URLField()
    image = models.ImageField()
    cast = models.TextField(max_length=150)
    #genres = models.ManyToManyField('Genre')    hata var

    def __str__(self):
        return self.title
    

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=10)
    expiration_date = models.CharField(max_length=7)  # Örneğin: 'MM/YYYY' formatında
    cvv = models.CharField(max_length=3)


    def __str__(self):
        return f"{self.movie.title} - {self.user.username}"


