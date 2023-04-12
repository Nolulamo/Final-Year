from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


def home(request):
    return render(request, 'dashboard/home.html', {})

def index(request):
    
    return render(request, 'dashboard/dashboard.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['Users', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items =[qs_count, 12, 25, 15, 20, 9, 10]
        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)
    
def post_entry(request):

    if request.method == 'POST':
        post_data = request.body
        
    return HttpResponse('Hey there im working')