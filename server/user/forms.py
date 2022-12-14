from django.contrib.auth import get_user_model

from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password', 'nickname', 'user_type']



