from django.db import models

from django.core.exceptions import ValidationError
from model_utils import Choices

# Create your models here.

def validate_gender(value):
    # validating gender field
    if len(value) > 1:
        raise ValidationError('Gender must be of 1 char')
    
class Customer(models.Model):
    male   = 'M'
    female = 'F'
    # gender_choices = [ (male, 'Male'), (female, 'Female')] # list of tuples for choices
    # tuple: (<value_to_store_in_db>, <humane_readable_to_be_displayed>)
    gender_choices = Choices((male, 'Male'), (female, 'Female')) # cleanier way
    name   = models.CharField(max_length=250)
    dob    = models.DateField(null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    gender  = models.CharField(max_length=1, validators=[validate_gender],
                               choices=gender_choices)
    cell    = models.IntegerField(unique=True)
    email   = models.EmailField(max_length=250, default="", null=True)

    def to_dict(self):
        c = dict(self.__dict__)
        del c['_state']
        return c
