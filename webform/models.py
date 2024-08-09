from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999999999)])

class BackgroundInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=100)
    TelephoneNumber = models.PositiveBigIntegerField()
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=6)
    MaritalStatus = models.CharField(max_length=10)
    EmailAddress = models.EmailField(null=True, blank=True)
    Nationality = models.CharField(max_length=100)
    Ugandan_Identification_Number = models.CharField(max_length=100, null=True, blank=True)
    Refugee_Number = models.CharField(max_length=100, null=True, blank=True)
    settlement = models.CharField(max_length=255, blank=True, null=True)
    district_city = models.CharField(max_length=255, blank=True, null=True)
    subcounty_division = models.CharField(max_length=255, blank=True, null=True)
    parish_ward = models.CharField(max_length=255, blank=True, null=True)
    village_cell_zone = models.CharField(max_length=255, blank=True, null=True)


# Model to store business information
class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year_of_establishment = models.PositiveIntegerField()
    sector = models.CharField(max_length=255)
    number_of_employees_male = models.IntegerField()
    number_of_employees_female = models.IntegerField()
    total_employees = models.IntegerField()
    revenue_per_annum = models.DecimalField(max_digits=12, decimal_places=2)
    location_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Model to store trade association information
class TradeAssociation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_group = models.CharField(max_length=255)
    website_link = models.URLField(blank=True, null=True)
    is_registered = models.BooleanField()
    contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_person_email = models.EmailField(blank=True, null=True)
    

# Model to store trade association members
class TradeAssociationMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trade_association = models.ForeignKey(TradeAssociation, related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)  # 'Male' or 'Female'

    def __str__(self):
        return f"{self.name} ({self.phone_number})"

# Model to store women entrepreneurship platform responses
class WomenEntrepreneurshipPlatform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    how_did_you_hear = models.CharField(max_length=50)
    preferred_communication_method = models.CharField(max_length=50)
    involved_in_empowerment = models.BooleanField()
    confirmed = models.BooleanField()