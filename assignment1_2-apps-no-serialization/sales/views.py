from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views
from rest_framework import status
import sales.models

# Create your views here.
class CustomerView(views.APIView):

    def get(self, request, pk=None, format=None):
        # get customer
        if pk:
            rec = sales.models.Customer.objects.get(id=int(pk))
            return views.Response(rec.to_dict())

        recs = sales.models.Customer.objects.all()
        #return views.Response(recs, status=HTTP_200_OK)
        return views.Response([rec.to_dict() for rec in recs])

    def post(self, request, format=None):
        # write something to the db 
        cust = sales.models.Customer(**request.data)
        cust.save()
        msg={'id': cust.id}
        return views.Response(msg, status=status.HTTP_201_CREATED)


def home_view(request):
    return render(request, "home_view.html")
