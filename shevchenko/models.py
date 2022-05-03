from django.db import models

# Create your models here.


from django.db import models


class ArtWay(models.Model):
    way_name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.way_name

    class Meta:
        verbose_name = 'Напрямки творчості'
        verbose_name_plural = 'Напрямки творчості'


class Genre(models.Model):
    name = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанри'
        verbose_name_plural = 'Жанри'


class ArtPeriod(models.Model):
    art_period_name = models.CharField(max_length=40)
    period_start_date = models.DateField()
    period_finish_date = models.DateField()

    def __str__(self):
        return self.art_period_name

    class Meta:
        verbose_name = 'Періоди творчості'
        verbose_name_plural = ' Періоди творчості'


class ArtList(models.Model):
    name = models.CharField(max_length=100)
    date_of_writing = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    art_way = models.ForeignKey(ArtWay, on_delete=models.CASCADE)
    art_period = models.ForeignKey(ArtPeriod, on_delete=models.CASCADE)
    notes = models.CharField(max_length=300)

    class Meta:
        verbose_name = ' Cписок художніх творів'
        verbose_name_plural = ' Cписок художніх творів'


class Collection(models.Model):
    name = models.CharField(max_length=30)
    date_of_writing = models.DateField()
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Збірки творів'
        verbose_name_plural = 'Збірки творів'


class LiteratureList(models.Model):
    name = models.CharField(max_length=100)
    date_of_writing = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    art_way = models.ForeignKey(ArtWay, on_delete=models.CASCADE)
    art_period = models.ForeignKey(ArtPeriod, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)


    class Meta:
        verbose_name = ' Cписок літературних творів'
        verbose_name_plural = " Cписок літературних творів"


class Schools(models.Model):
    school_name = models.CharField(max_length=30)
    start_learning_date = models.DateField()
    end_learning_date = models.DateField()
    notes = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Школи'
        verbose_name_plural = "Школи"


class PoetViews(models.Model):  # Погляди шивченко
    view_topic = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name = ' Погляди Шевченка '
        verbose_name_plural = " Погляди Шевченка"
