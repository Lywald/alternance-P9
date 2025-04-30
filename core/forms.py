from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Si tu avais des champs personnalisés sur ton modèle User,
        # tu pourrais les ajouter ici dans la liste 'fields'
        # Par exemple: fields = UserCreationForm.Meta.fields + ('nom_champ_perso',)
        fields = UserCreationForm.Meta.fields 