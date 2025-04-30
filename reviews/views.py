from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Value, Q
from itertools import chain
from django.utils import timezone
from datetime import datetime

from .models import Ticket, Review

class FeedView(LoginRequiredMixin, ListView):
    template_name = 'reviews/feed.html'
    context_object_name = 'feed'
    
    def get_queryset(self):
        # Récupérer l'utilisateur connecté
        user = self.request.user
        
        # Récupérer les tickets et reviews de l'utilisateur
        user_tickets = Ticket.objects.filter(user=user)
        user_reviews = Review.objects.filter(user=user)
        
        # Récupérer les tickets et reviews des utilisateurs que l'utilisateur suit
        followed_users = user.following.values_list('followed_user', flat=True)
        followed_tickets = Ticket.objects.filter(user__in=followed_users)
        followed_reviews = Review.objects.filter(user__in=followed_users)
        
        # Récupérer les reviews en réponse aux tickets de l'utilisateur
        reviews_of_user_tickets = Review.objects.filter(ticket__in=user_tickets)
        
        # Ajouter un champ pour différencier les types d'objets
        user_tickets = user_tickets.annotate(content_type=Value('TICKET', CharField()))
        user_reviews = user_reviews.annotate(content_type=Value('REVIEW', CharField()))
        followed_tickets = followed_tickets.annotate(content_type=Value('TICKET', CharField()))
        followed_reviews = followed_reviews.annotate(content_type=Value('REVIEW', CharField()))
        reviews_of_user_tickets = reviews_of_user_tickets.annotate(content_type=Value('REVIEW', CharField()))
        
        # Combiner tous les objets dans une seule liste
        combined_feed = sorted(
            chain(user_tickets, user_reviews, followed_tickets, followed_reviews, reviews_of_user_tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
        
        return combined_feed
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        # Ajouter d'autres données de contexte si nécessaire
        return context
