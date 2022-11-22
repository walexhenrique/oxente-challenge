from django.db import models

from accounts.models import User


class Residence(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Dono')
    title = models.CharField(max_length=120, verbose_name='Título')
    slug = models.SlugField()
    description = models.TextField()
    price = models.FloatField(verbose_name='Preço')

    street = models.TextField(verbose_name='Rua')
    district = models.TextField(verbose_name='Bairro')
    number = models.CharField(max_length=5, blank=True, null=True, default='')
    complement = models.TextField(verbose_name='Complemento', default='')
    is_published = models.BooleanField(verbose_name='Publicado', default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    bathrooms = models.PositiveIntegerField(verbose_name='Quantidade de banheiros')
    bedrooms = models.PositiveIntegerField(verbose_name='Quantidade de quartos')

    latitude = models.FloatField(default=0)  # Verificar se isso vai ser usado
    longitude = models.FloatField(default=0)  # Verificar se isso vai ser usado

    def __str__(self) -> str:
        return self.title


class Photo(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, verbose_name='Residência', related_name='photos')
    image = models.ImageField(upload_to='residences/pictures/%Y/%m/%d/')

    def __str__(self) -> str:
        return self.image.url