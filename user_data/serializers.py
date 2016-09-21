from rest_framework import serializers
from user_data.models import Customer, Billing


class UserList(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = ('url',
                  'cust_id',
                  'name',
                  'phone',
                  'emailid',
                  'DOB',
                  'address',
                  'joining_date',
                  'deleted')
        extra_kwargs = {
            'url': {
                 'view_name': 'user-detail',
                'lookup_field': 'cust_id'
            }
        }


class BillList(serializers.ModelSerializer):

    class Meta:
        model = Billing
