from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile.
    Stores details such as the associated user, and favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associated user
    favorite_city = models.CharField(max_length=64, blank=True)   # Favorite city of the user

    class Meta:
        verbose_name_plural = "Profiles"   # Plural name for the model in the admin interface

    def __str__(self):
        """
        Returns a string representation of the profile.
        """
        return self.user.username  # Username of the associated user
