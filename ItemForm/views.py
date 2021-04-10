from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from .models import Item
from .import forms

# Create your views here.

def item_list(request):
    items = Item.objects.all().order_by('-inserted_time')
    total_expense = round(Item.objects.aggregate(Sum('cost'))['cost__sum'],2)
    total_income = round(Item.objects.aggregate(Sum('sold_price'))['sold_price__sum'],2)
    total_profit = total_income - total_expense
    total_ROI = (total_profit/total_expense) * 100
    context = {
        'items': items, 
        'total_expense': total_expense,
        'total_income': total_income,
        'total_profit': total_profit,
        'total_ROI': total_ROI
        }
    return render(request, 'ItemForm/item_list.html', context=context)


def create_item(request):
    if request.method == "POST":
        form = forms.ItemForm(request.POST)

        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('ItemForm:item_list'))
    else:
        form = forms.ItemForm()
    context = {
        "form": form,
    }
    return render(request, 'ItemForm/create_item.html',context=context)


def update_item(request, pk): 
    item = Item.objects.get(id=pk)
    context = {
        'description': item.description, 
        'cost': item.cost,
        'sold_price': item.sold_price,
        }

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        print('post request')
        if form.is_valid():
            print('debugging2')
            form.save()
            return HttpResponseRedirect(reverse('ItemForm:item_list'))
        print('no valid')

    return render(request, 'ItemForm/update_item.html', context=context)

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    context = { 'item' : item }
    
    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect(reverse('ItemForm:item_list'))

    return render(request, 'ItemForm/delete_item.html', context=context)
