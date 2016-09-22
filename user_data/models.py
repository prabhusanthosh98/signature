from django.db import models
from django.utils import timezone
import string, random
# Create your models here.

def stringkey(N):
    return(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N)))

SERVICE_TYPES = (
    ('Head Massage', 'Head Massage'),
    ('Full Body Massage', 'Full Body Massage'),
    ('Hair Cut', 'Hair Cut'),
    ('Shave', 'Shave'),
    ('Facial', 'Facial'),
)


class Customer(models.Model):
    cust_id = models.CharField(max_length=36, unique=True, editable=False, default=stringkey(6), primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True)
    emailid = models.EmailField(max_length=256, null=True, blank=True)
    DOB = models.DateField(auto_now=False, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now_add=True, editable=False, blank=False)

    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.cust_id + '|' + self.name


class Billing(models.Model):
    cust_id = models.ForeignKey('Customer')
    service = models.CharField(max_length=512)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True, editable=False, blank=False)
    deleted = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.cust_id.name + '|' + self.service