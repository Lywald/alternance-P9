from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True, verbose_name="Description")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name='tickets', verbose_name="Utilisateur")
    image = models.ImageField(upload_to='tickets/', null=True, blank=True, verbose_name="Image")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ['-time_created']

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name='reviews', verbose_name="Ticket")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note")
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='reviews', verbose_name="Utilisateur")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    def __str__(self):
        return f"{self.headline}"
    
    class Meta:
        verbose_name = "Critique"
        verbose_name_plural = "Critiques"
        ordering = ['-time_created']
