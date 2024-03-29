from django.http import HttpResponse
from django.shortcuts import render

from .models import Template


def index(request):
    '''Get all Templates from the database and return them as a dict.'''
    
    
    queryset =  Template.objects.all()
    context = { 'object_list' : queryset,
                'title': 'List'
    }
    
    
    return render(request, 'base.html', context)