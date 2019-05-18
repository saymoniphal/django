from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views
from rest_framework import status
import sales.models

# Create your views here.
class CustomerView(views.APIView):

    def get(self, request, pk=None, format=None):
        # get customer per id
        if pk:
            rec = sales.models.Customer.objects.get(id=int(pk))
            return views.Response(rec.to_dict())

        # get all customer
        recs = sales.models.Customer.objects.all()
        #return views.Response(recs, status=HTTP_200_OK)
        return views.Response([rec.to_dict() for rec in recs])

    def post(self, request, format=None):
        # add customer to the database
        cust = sales.models.Customer(**request.data)
        cust.save()
        msg={'id': cust.id}
        return views.Response(msg, status=status.HTTP_201_CREATED)


    def put(self, request, pk, format=None):
        # update customer information
        cust = sales.models.Customer.objects.get(id=int(pk))
        cust.__dict__.update(**request.data)
        cust.save()
        return views.Response()

    def delete(self, request, pk):
        # delete customer with given id
        cust = sales.models.Customer.objects.get(id=int(pk)) 
        resp = cust.delete()
        return views.Response(resp)

def home_view(request):
    return render(request, "home_view.html")
