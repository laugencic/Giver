from django.shortcuts import render
import requests
from .models import Profile
from django.contrib import messages

#imports the decorator that modifies how a function behaves 
#tells django to only allow post requets
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def chat(request):
    message=request.data.get('message')
    reply=f"You said {message}"

    return Response({
        'reply':reply
    })


@api_view(['POST'])
def details(request):
    fname=request.data.get('fname')
    lname=request.data.get('lname')
    email=request.data.get('email')
    
    Profile.objects.create(
        fname=fname,
        lname=lname,
        email=email
    )

    return Response({
        'message':f"Account for {fname} has been created"
    })


