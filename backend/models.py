from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from datetime import datetime

# recuperer l'heure actuelle


def get_now():
    now = datetime.now()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    time = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    today_date = day+month+year+time+minute+second
    return today_date


# Status

PENDING = "En attente de collecte"
REPOSITORY = "Avec la société de livraison"
IN_PROGRESS = "Avec le livreur"
ON_GOING = "En cours"
DELIVERED = "Livré"
# Sexe
MALE = "Masculin"
FEMALE = "Feminin"

STATUS = (
    (DELIVERED, DELIVERED),
    (PENDING, PENDING),
    (IN_PROGRESS, IN_PROGRESS),
    (REPOSITORY, REPOSITORY)
)
STATUSLIV = (
    (DELIVERED, DELIVERED),
    (ON_GOING, ON_GOING)
)

SEX = (
    (MALE, MALE),
    (FEMALE, FEMALE),
)


class Client(models.Model):
    full_name = models.CharField(
        "Nom complet",
        max_length=255,
        null=True,
        blank=True
    )
    email = models.EmailField("Email", null=True, blank=True)
    phone = models.CharField("Telephone", max_length=20, null=True, blank=True)
    address = models.CharField(
        "Adresse Client",
        max_length=150,
        null=True,
        blank=True
    )
    website = models.URLField("Website", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    sexe = models.CharField(
        "sexe",
        max_length=10,
        choices=SEX,
        null=True,
        blank=True
    )
    sales_revenue_product = models.DecimalField(
        "C-A produits",
        max_digits=50,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
    )
    sales_revenue_delivery = models.DecimalField(
        "C-A livraison", max_digits=50, decimal_places=2, default=0.0, null=True)
    first_delivery_date = models.DateTimeField(
        "Date de premiere livraison",
        null=True,
        blank=True,
        auto_now=False,
        auto_now_add=False
    )
    last_delivery_date = models.DateField(
        "Date de dernière livraison",
        null=True,
        blank=True,
        auto_now=False,
        auto_now_add=False
    )
    number_deliveries = models.IntegerField(
        "Nombre de livraison",
        default=0,
        null=True,
        blank=True
    )
    created_at = models.DateField(
        "Date Creation Client",
        null=True,
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.full_name


class Article(models.Model):
    designation = models.CharField(
        "Désignation",
        max_length=255,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        "Prix unitaire",
        max_digits=10,
        decimal_places=2,
        null=True
    )
    size = models.CharField(
        "Poids",
        max_length=150,
        null=True, blank=True
    )
    color = models.CharField(
        "Couleur produit",
        max_length=150,
        null=True
    )
    modele = models.CharField(
        "Modele",
        max_length=150,
        null=True
    )
    date_creation = models.DateField(
        "Date Creation Article",
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
     )

    def __str__(self):
        return self.designation


class Parcel(models.Model):
    articles = models.ManyToManyField(Article, blank=True)
    tracking_number = models.CharField(
        "Numéro tracking",
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )
    weight = models.DecimalField(
        "Poids colis",
        default=0,
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    client = models.ForeignKey(
        Client,
        models.SET_NULL,
        null=True,
        blank=True)
    status = models.CharField(
        "Status colis",
        max_length=150,
        choices=STATUS,
        default=PENDING
    )
    comment = models.CharField(
        "commentaire colis",
        max_length=150,
        default="vide",
        null=True,
        blank=True
    )
    date_delivery = models.DateField(
        "Date livraison colis",
        null=True,
        blank=True
    )
    isChecked = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )
    date_creation = models.DateField(
        "Date création colis",
        auto_now_add=True
    )
    delivery_price = models.DecimalField(
        "Prix de livraison",
        default=0,
        max_digits=100,
        decimal_places=2,
        blank=True,
        null=True
    )
     
    def __str__(self):
        return self.tracking_number


def pre_save_tracking_number(sender, instance, *args, **kwargs):
    parcel = "COL"
    parcel_date = get_now()
    if not instance.tracking_number:
        instance.tracking_number = parcel+parcel_date


pre_save.connect(pre_save_tracking_number, sender=Parcel)


class Delivery(models.Model):
    status = models.CharField(
        "Status livraison",
        max_length=50,
        choices=STATUSLIV,
        null=True,
        blank=True,
        default = ON_GOING
    )
    delivery_number = models.CharField(
        "Numéro livraison",
        max_length=50,
        null=True,
        blank=True,
        unique=True
    )
    parcels = models.ManyToManyField(
        Parcel,
        blank=True,
        null = True
    )
    commentaire = models.CharField(
        "commentaire tournée",
        max_length=100,
        default="rien à signaler",
        null=True,
        blank=True
    )
    date_creation = models.DateField(
        "Date Creation Livraison",
        auto_now_add=True
    )
    date_livraison = models.DateField(
        "Date Livraison",
        null=True,
        blank=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
     )
    def __str__(self):
        return self.delivery_number


def pre_save_delivery_number(sender, instance, *args, **kwargs):
    delivery = "LIV"
    delivery_date = get_now()
    if not instance.delivery_number:
        instance.delivery_number = delivery+delivery_date


pre_save.connect(pre_save_delivery_number, sender=Delivery)


class ParcelQuantity(models.Model):
    quantity = models.PositiveIntegerField(
        "Nombre de produit",
        default=0,
        null=True
    )
    id_article = models.IntegerField(blank=True, null=True)
    id_parcel = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "quantities"
