from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import (SessionAuthentication,
                                           BasicAuthentication)
from django.db.models import Q
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from user_data.forms import User, Bill, SearchField
from user_data.models import Customer, Billing
from user_data.serializers import UserList, BillList

def add_user(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            user_data = form.save(commit=True)
            user_data.save()
            # return redirect(reverse('addservice', kwargs={'cust_id': user_data.cust_id}))
            return redirect(reverse('user-detail', kwargs={'cust_id': user_data.cust_id}))
        else:
            return render(request, 'test.html', {'form': form})
    else:
        new_form = User()
    return render(request, 'test.html', {'form': new_form})



def add_service(request, cust_id, id=None):
    cust = list(Customer.objects.filter(cust_id=cust_id))
    if request.method == "POST":
        if id != None:
            bill = Billing.objects.get(id=id)
            form = Bill(request.POST, instance=bill)
        else:
            form = Bill(request.POST)
        if form.is_valid():
            service_data = form.save(commit=False)
            service_data.cust_id = cust[0]
            service_data.save()
            return redirect(reverse('user-detail', kwargs={'cust_id': cust[0].cust_id}))
        else:
            return render(request, 'test.html', {'form': form, 'name':cust[0].name})
    else:
        if id != None:
            bill = Billing.objects.get(id=id)
            new_form = Bill(instance=bill)
        else:
            new_form = Bill()
    return render(request, 'test.html', {'form': new_form, 'name':cust[0].name})

@api_view(['POST'])
@authentication_classes((SessionAuthentication,
                         BasicAuthentication))
def serach_user(request):
    if request.method == 'POST':
        qset = Q()
        for term in request.data['data'].split():
            qset |= Q(name__contains=term)
            qset |= Q(phone__contains = term)
            qset |= Q(phone__contains=term)
        matching_results = list(Customer.objects.filter(qset))
        serializer = UserList(matching_results, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes((SessionAuthentication,
                         BasicAuthentication))
def get_bill_history(request, cust_id):
    if request.method == 'GET':
        matching_results = list(Billing.objects.filter(cust_id__cust_id=cust_id))
        serializer = BillList(matching_results, many=True)
        return Response(serializer.data)


def serach_user_v1(request):
    if request.method == "POST":
        new_form = SearchField(request.POST)
        print(request.POST)
        qset = Q()
        if not len(request.POST['search']) == 0:
            for term in request.POST['search'].split():
                qset |= Q(name__contains=term)
                qset |= Q(phone__contains=term)
                qset |= Q(emailid__contains=term)
            matching_results = list(Customer.objects.filter(qset))
            if matching_results == []:
                matching_results = None
            else:
                matching_results = UserList(matching_results, context={'request': request}, many=True)
                matching_results = matching_results.data
            return render(request, 'search.html', {'form': new_form,
                                                   'object': matching_results})
    else:
        new_form = SearchField()
    return render(request, 'search.html', {'form': new_form,
                                           'object': None})

def get_bill_history_v1(request, cust_id):
    if request.method == 'GET':
        matching_results = list(Billing.objects.filter(cust_id__cust_id=cust_id))
        user = Customer.objects.get(cust_id=cust_id)
        if matching_results == []:
            data = None
        else:
            serializer = BillList(matching_results, many=True)
            data = serializer.data
        url = reverse('addservice', kwargs={'cust_id': cust_id})
        return render(request, 'bill_history.html', {'object': data, 'url': url, 'name':user.name})