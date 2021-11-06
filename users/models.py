from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    class ROLE_CHOICES(models.TextChoices):
        USER = 'user',
        ADMIN = 'admin',

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='role')
    role = models.CharField(max_length=20,
                            choices=ROLE_CHOICES.choices,
                            default=ROLE_CHOICES.USER)

    def __str__(self):
        return self.user.username

    @property
    def is_admin(self):
        if self.role == 'admin' or self.is_superuser:
            return True
        return False