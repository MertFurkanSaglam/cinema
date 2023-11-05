from django.contrib import admin
from .models import Movies, Seanslar,Salon,Genres,ComingSoonMovie


class Admin(admin.ModelAdmin):
    list_display = ("title","name","director","cast","slug",) #admin panelinde nelerin gözükmesini istiyorsun
    # list_editable = ("twod",) #hangilerini ayarlamak istiyorsun(text olanları değiştirmeyi denedim yapamadım)
    search_fields = ("title","description",) #arama butonu nerede arama yapacağını seçiyorsun
    readonly_fields = ("slug",) #edit yapılmasını engelleyip sadece okunmasına olanak sağlıyor
    list_filter = ("is_active","is_home",) #sağ tarafta çıkan kısa filtreleme yolu


admin.site.register(Movies)
admin.site.register(Seanslar)
admin.site.register(Salon)
admin.site.register(Genres)
admin.site.register(ComingSoonMovie)