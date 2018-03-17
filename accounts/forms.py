from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateSignupForm(UserCreationForm):
    class Meta:
        fields=('username','email','password1','password2')
        model = get_user_model()
