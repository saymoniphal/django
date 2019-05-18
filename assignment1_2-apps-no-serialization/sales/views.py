from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views

# Create your views here.
class CustomerView(views.APIView):

    def get(self, request, format=None):
        # get customer
        data = {'customer1': {}, 'customer2': {}}
        return views.Response(data)

    def post(self, request, pk, format=None):
        # write something to the db
        
        return views.Response('Sucessfully created customer')


def home_view(request):
    return render(request, "home_view.html")
