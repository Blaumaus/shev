from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import routers
from .serializers import LiteratureListSerializer, GenreSerializer, ArtListSerializer, SchoolsSerializer, \
    ArtWaySerializer, CollectionSerializer, ArtPeriodSerializer, PoetViewsSerializer
from .models import Schools, ArtPeriod, ArtWay, ArtList, LiteratureList, Collection, PoetViews, Genre


# class

class LiteratureListViewSet(viewsets.ModelViewSet):
    # queryset = LiteratureList.objects.filter(date_of_writing__year=2005).select_related()  # 1st query  !!!!!!!!!!!
    queryset = LiteratureList.objects.all()
    print(queryset.query)  # перевод в raw sql !
    """
    SELECT "shevchenko_literaturelist"."id", "shevchenko_literaturelist"."name", "shevchenko_literaturelist"."date_of_writing", "shevchenko_literaturelist"."genre_id", "shevchenko_literaturelist"."art_way_id", "shevchenko_literaturelist"."art_period_id", "shevchenko_lit
    eraturelist"."collection_id", "shevchenko_literaturelist"."notes", "shevchenko_genre"."id", "shevchenko_genre"."name", "shevchenko_genre"."notes", "shevchenko_artway"."id", "shevchenko_artway"."way_name", "shevchenko_artway"."description", "shevchenko_artperiod"."id
    ", "shevchenko_artperiod"."art_period_name", "shevchenko_artperiod"."period_start_date", "shevchenko_artperiod"."period_finish_date", "shevchenko_collection"."id", "shevchenko_collection"."name", "shevchenko_collection"."date_of_writing", "shevchenko_collection"."no
    tes" FROM "shevchenko_literaturelist" INNER JOIN "shevchenko_genre" ON ("shevchenko_literaturelist"."genre_id" = "shevchenko_genre"."id") INNER JOIN "shevchenko_artway" ON ("shevchenko_literaturelist"."art_way_id" = "shevchenko_artway"."id") INNER JOIN "shevchenko_a
    rtperiod" ON ("shevchenko_literaturelist"."art_period_id" = "shevchenko_artperiod"."id") INNER JOIN "shevchenko_collection" ON ("shevchenko_literaturelist"."collection_id" = "shevchenko_collection"."id") WHERE "shevchenko_literaturelist"."date_of_writing" BETWEEN 20
    """
    serializer_class = LiteratureListSerializer


class GenreSchoolsViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()  # 1st query  !!!!!!!!!!!
    # routers.get_api_root_view().cls.__name__ = "Жанри"
    print(queryset.query)
    """
    SELECT "shevchenko_genre"."id", "shevchenko_genre"."name", "shevchenko_genre"."notes" FROM "shevchenko_genre"
    """
    serializer_class = GenreSerializer
    print(queryset.query)


class ArtListViewSetDescDOW(viewsets.ModelViewSet):  # date off writing
    # queryset = ArtList.objects.all().order_by('-date_of_writing')  # Descending
    queryset = ArtList.objects.all()
    serializer_class = ArtListSerializer
    """
    SELECT "shevchenko_artlist"."id", "shevchenko_artlist"."name", "shevchenko_artlist"."date_of_writing", 
    "shevchenko_artlist"."genre_id", "shevchenko_artlist"."art_way_id", "shevchenko_artlist"."art_period_id", 
    "shevchenko_artlist"."notes" FROM "shevchenko_artlist" WHERE
    """
    print(queryset.query)


class CollectionView(viewsets.ModelViewSet):
    # queryset = ArtList.objects.all().order_by('name')  # ASC
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    """
     SELECT "shevchenko_artlist"."id", "shevchenko_artlist"."name", "shevchenko_artlist"."date_of_writing",
     "shevchenko_artlist"."genre_id", "shevchenko_artlist"."art_way_id", "shevchenko_artlist"."art_period_id", 
     "shevchenko_artlist"."notes" FROM "shevchenko_artlist" OR
     DER BY "shevchenko_artlist"."name" ASC
    """

    print(queryset.query)


class ArtListViewSetSpecificArtPeriod(viewsets.ModelViewSet):
    #queryset = ArtList.objects.filter(art_period=2002)
    queryset = ArtList.objects.all()
    serializer_class = ArtListSerializer

    """
    SELECT "shevchenko_artlist"."id", "shevchenko_artlist"."name", "shevchenko_artlist"."date_of_writing", "shevchenko_artlist"."genre_id", 
    "shevchenko_artlist"."art_way_id", "shevchenko_artlist"."art_period_id", "shevchenko_artlist"."notes" FROM "shevchenko_artlist" 
    WHERE "shevchenko_artlist"."art_period_id" = 2002

    """
    print(queryset.query)


class SchoolsView(viewsets.ModelViewSet):
    # queryset = Schools.objects.filter(start_learning_date__range=["1800-10-02", "1900-05-02"])
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer
    print(queryset.query)


class SchoolsViewEndDate_From_Date_To(viewsets.ModelViewSet):
    #queryset = Schools.objects.filter(end_learning_date__range=["1800-10-02", "1900-05-02"])
    queryset = Schools.objects.all()
    """
    SELECT "shevchenko_schools"."id", "shevchenko_schools"."school_name", "shevchenko_schools"."start_learning_date", 
    "shevchenko_schools"."end_learning_date", "shevchenko_schools"."notes" FROM "shevchenko_schools" WHERE "shevchenko_schools"
    ."end_learning_date__range" BETWEEN 1800-10-02 AND 1900-05-02
    """
    serializer_class = SchoolsSerializer
    print(queryset.query)


class ArtPeriodView(viewsets.ModelViewSet):
    #queryset = ArtWay.objects.filter(way_name__endswith='ізм')
    queryset = ArtPeriod.objects.all()
    """
    SELECT "shevchenko_artway"."id", "shevchenko_artway"."way_name", "shevchenko_artway".
    "description" FROM "shevchenko_artway" WHERE "shevchenko_artway"."way_name" LIKE %ізм ESCAPE '\'
    """
    serializer_class = ArtPeriodSerializer
    print(queryset.query)

class ArtWayView(viewsets.ModelViewSet):
    #queryset = ArtWay.objects.filter(way_name__endswith='ізм')
    queryset = ArtWay.objects.all()
    """
    SELECT "shevchenko_artway"."id", "shevchenko_artway"."way_name", "shevchenko_artway".
    "description" FROM "shevchenko_artway" WHERE "shevchenko_artway"."way_name" LIKE %ізм ESCAPE '\'
    """
    serializer_class = ArtWaySerializer
    print(queryset.query)

class PoetViewsView(viewsets.ModelViewSet):
    #queryset = ArtWay.objects.filter(way_name__endswith='ізм')
    queryset = PoetViews.objects.all()

    serializer_class = PoetViewsSerializer
    print(queryset.query)
