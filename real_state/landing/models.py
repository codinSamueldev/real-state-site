from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Properties(models.Model):
    title = models.TextField(max_length=255, blank=False, null=False, verbose_name="Title")
    description = models.TextField(max_length=255, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(10000, message="Starting prices for properties must start at $10,000.")], verbose_name="Price") # Minimum price is $10,000 and max price up to $99,000,000.00
    location = models.TextField(max_length=1000, blank=False, null=False, verbose_name="Location/Address")
    property_type = models.TextField(max_length=255, blank=False, null=False, verbose_name="Type of property (Condo, house...)")
    bedrooms = models.PositiveSmallIntegerField(verbose_name="Bedrooms") # Values from 0 to 32767.
    bathrooms = models.PositiveSmallIntegerField(verbose_name="Bathrooms") # Values from 0 to 32767.
    area = models.PositiveSmallIntegerField(verbose_name="Square feet of propertie") # Values from 0 to 32767 square feet.
    picture = models.ImageField(upload_to="properties_pics/", blank=True, null=True, verbose_name="Property high-value picture.")
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Publication date")

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-price"]

