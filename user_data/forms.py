from django import forms
from user_data.models import Customer, Billing, SERVICE_TYPES
from django.forms.extras.widgets import SelectDateWidget



class User(forms.ModelForm):
    DOB = forms.CharField(widget=SelectDateWidget(years=range(1980, 2012)))
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'emailid', 'DOB', 'address', 'deleted']

class Bill(forms.ModelForm):
    service = forms.MultipleChoiceField(choices=SERVICE_TYPES, widget=forms.CheckboxSelectMultiple())
    def clean_my_field(self):
        if len(self.cleaned_data['my_field']) > 3:
            raise forms.ValidationError('Select no more than 3.')
        return self.cleaned_data['my_field']

    class Meta:
        model = Billing
        fields = ['cust_id', 'service', 'amount', 'deleted', 'paid']



class SearchField(forms.Form):
    search = forms.CharField(label='search', max_length=100)