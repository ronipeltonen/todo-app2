from django.db import models

class Kategoria(models.Model):
    nimi = models.CharField(max_length=100)

    def __str__(self):
        return self.nimi


class Tehtava(models.Model):
    otsikko = models.CharField(max_length=200)
    kategoria = models.ForeignKey(
        Kategoria,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    tehty = models.BooleanField(default=False)

    # on_delete-säännöt
    #
    # CASCADE: Kun kategoria poistetaan,
    #   niin poistetaan kaikki sen tehtävät
    # RESTRICT: Kategoriaa ei anneta poistaa
    #   ennen kuin tehtävät on (käsin) poistettu
    # SET_NULL: Jos kategoria poistetaan,
    #   niin sen kaikki tehtävät saavat kategorian arvoksi NULL
    # SET_DEFAULT: Jos kategoria poistetaan,
    #   niin sen kaikki tehtävät saavat kategorian arvoksi oletusarvon

    def __str__(self):
        return self.otsikko
