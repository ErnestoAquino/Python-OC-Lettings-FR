"""
Defines two models, Address and Letting, for managing physical addresses and property lettings.

Models: - Address: Represents a physical address with street number, street name, city, state,
ZIP code, and country code.
- Letting: Represents a property available for rent, storing details such as title and address.

"""


from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.
    Stores details such as street number, street name, city, state, ZIP code, and country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])   # Street number
    street = models.CharField(max_length=64)  # Street name
    city = models.CharField(max_length=64)  # City
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"  # Plural name for the model in the admin interface

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        return f'{self.number} {self.street}'  # Concatenated street number and name


class Letting(models.Model):
    """
    Represents a property available for rent.
    Stores details such as title and address.
    """
    title = models.CharField(max_length=256)  # Title of the letting
    address = models.OneToOneField(Address, on_delete=models.CASCADE)   # Address of the letting

    class Meta:
        verbose_name_plural = "Lettings"  # Plural name for the model in the admin interface

    def __str__(self):
        """
        Returns a string representation of the letting.
        """
        return self.title  # Title of the letting
