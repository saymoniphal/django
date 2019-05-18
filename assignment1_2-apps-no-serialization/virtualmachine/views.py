from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views

import psutil

# Create your views here.
class TempCPUView(views.APIView):

    def get(self, request, format=None):
        temps = psutil.sensors_temperatures()
        if temps and 'coretemp' in temps:
            coretemp = temps['coretemp'][0].current
            return Response("CPU Temperature: %.1f oC" %(coretemp))
        if not temps:
            return None

class NumCPUView(views.APIView):
    def get(self, request, format=None):
        return Response("Num CPU: %d Cores" %(psutil.cpu_count()))


class RAMView(views.APIView):
    def get(self, request, format=None):
        ram = psutil.virtual_memory()
        fac = 1024 ** 3 # B (bytes) to GB
        if ram:
            return Response("Total: %.1f GB, Used: %.1f GB Available: %.1f GB"
                            %((ram.total/fac), (ram.used/fac),
                              (ram.available/fac)))


class HDDView(views.APIView):
    def get(self, request, format=None):
        disk = psutil.disk_usage('/')
        fac = 1024 ** 3 # B (bytes) to GB
        if disk:
            return Response("Total: %0.1f GB, Used: %0.1f GB, Available: %0.1f GB"
                            %(disk.total/fac, disk.used/fac,
                              disk.free/fac))
