from django.shortcuts import render

from django.http import JsonResponse

from json import JSONEncoder
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
import datetime

@csrf_exempt
def submit_expense(request):
    ''' user submits an expense request'''
    
    #TODO: validate data, user might be fake, token might be fake, amount might be ...    
    
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    print(this_user)
    date = request.POST.get('date', datetime.datetime.now())
    Expense.objects.create(user = this_user, amount = request.POST['amount'], 
                           text = request.POST['text'], date = date)

    print(request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder = JSONEncoder)

@csrf_exempt
def submit_income(request):
    ''' user submits an income request'''
    
    #TODO: validate data, user might be fake, token might be fake, amount might be ...    
    
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    print(this_user)
    date = request.POST.get('date', datetime.datetime.now())
    Income.objects.create(user = this_user, amount = request.POST['amount'], 
                           text = request.POST['text'], date = date)

    print(request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder = JSONEncoder)