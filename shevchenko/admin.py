from django.contrib import admin
from .models import Schools, ArtPeriod, ArtWay, ArtList, LiteratureList, Collection, PoetViews, Genre

# Register your models here.

admin.site.register(Schools, verbose_name_plural = "stories")    # , ArtPeriod, ArtWay, ArtList, LiteratureList, Collection, PoetViews, Genre  verbose_name = 'школы'
admin.site.register(ArtPeriod)
admin.site.register(ArtWay)
admin.site.register(ArtList)
admin.site.register(LiteratureList)
admin.site.register(Collection)
admin.site.register(PoetViews)
admin.site.register(Genre)
