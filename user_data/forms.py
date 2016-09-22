from django import forms
from user_data.models import Customer, Billing, SERVICE_TYPES
from django.forms.extras.widgets import SelectDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'

class User(forms.ModelForm):
    # DOB = forms.CharField(widget=SelectDateWidget(years=range(1980, 2012)))
    DOB = forms.CharField(widget=DateInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':20}))
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'emailid', 'DOB', 'address', 'deleted']

class Bill(forms.ModelForm):
    service = forms.MultipleChoiceField(choices=SERVICE_TYPES,
                                        widget=forms.CheckboxSelectMultiple(),
                                        error_messages={'required': 'Please select the service availed!'})
    amount = forms.CharField(error_messages={'required': 'Amount needs to be filled!'})
    class Meta:
        model = Billing
        fields = ['service', 'amount', 'deleted', 'paid']



class SearchField(forms.Form):
    search = forms.CharField(label='Search', max_length=100,error_messages={'required':'Search field should not be empty'})