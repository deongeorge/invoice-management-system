from django.shortcuts import render,redirect,HttpResponse
from .forms import InvoiceForm , InvoiceSearchForm, InvoiceUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import bitly_api
import json
import os
import stripe

stripe.api_key = 'ebb843f49b1ec203be76ad667d9c30cae9865acd'

from flask import Flask, jsonify, request

def home(request):
    title = "Welcome..! Login to Manage Invoices"
    context = {
        "title": title,
    }
    return render(request, "base.html", context)

@login_required
def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Saved")
    context = {
        "form": form,
        "title":"New Invoice",
        "total_invoices": total_invoices,
    }
    return render(request, "entry.html", context)

@login_required
def list_invoice(request):
    title = 'Search Invoices'
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Invoice.objects.filter(
                                          Invoice_number__icontains=form['Invoice_number'].value(),
                                          Client_name__icontains=form['Client_name'].value()
                                         )
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request,"list_invoice.html", context)

@login_required
def update_invoice(request,pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_invoice')
    context = {
        "form":form
    }
    return render(request, 'entry.html', context)

@login_required
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method== 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render(request, 'delete_invoice.html')

stripe_urls = {
        40000: "https://buy.stripe.com/test_5kA4hfg0u9gbeNGbIK",
        60000: "https://buy.stripe.com/test_5kA9Bz6pUcsn0WQ8wA",
        80000: "https://buy.stripe.com/test_eVa7trcOi7839tm9AD",
        100000: "https://buy.stripe.com/test_eVadRPg0u8c7gVO288",
        125000: "https://buy.stripe.com/test_9AQeVTeWqbojfRKbIN",
        150000: "https://buy.stripe.com/test_4gw8xv01wcsncFy5kl",

    }

def Shorten_url(request,pk):
    Access_Token = "ebb843f49b1ec203be76ad667d9c30cae9865acd"
    connection = bitly_api.Connection(access_token=Access_Token)
    queryset = Invoice.objects.get(id=pk)
    stripe = stripe_urls.get(int(queryset.Amount))
    url = (stripe)

    shorten_url = connection.shorten(url)
    context = {
        "shorten_url": shorten_url.get('url'),
    }
    return render(request, 'link.html',context)

app = Flask(__name__)
@app.route('/pstatus', methods=['POST'])
def webhook(request):
    pst = ''
    if request.method == 'POST':
        queryset = Invoice.objects.get(id=pk)
        payload = queryset.data
        event = json.loads(payload)
        if event and event['type'] == 'checkout.session.completed':
            pst = "Paid"
        else:
            pst = "Not paid"
    context = {
        "pstatus": pst
    }

    return render(request, 'status.html', context)




